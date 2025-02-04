import scapy.all as scapy 
import os
import curses
from collections import defaultdict

# Basic config
THRESHOLD = 0  # Packet numbers from IP before block
SCAN_LOG = "scan_log.txt"
ip_requests = defaultdict(int)

# Function to block IP
def block_ip(ip):
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
    with open(SCAN_LOG, "a") as log:
        log.write(f"IP Blocked: {ip}\n")

# Port scanner detection function
def detect_port_scan(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src 
        if packet.haslayer(scapy.TCP):
            ip_requests[ip_src] += 1
            if ip_requests[ip_src] > THRESHOLD:
                block_ip(ip_src)
                del ip_requests[ip_src]

# Interactive Interface
def menu(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    h, w = stdscr.getmaxyx()
    title = "[ BLACK ICE - Security Monitoring]"

    # Initialize color pair
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    while True:
        stdscr.clear()
        stdscr.addstr(1, w//2 - len(title)//2, title, curses.A_BOLD | curses.color_pair(1))

        stdscr.addstr(3, 2, "1. Start Monitoring")
        stdscr.addstr(4, 2, "2. Watch logs")
        stdscr.addstr(5, 2, "3. Exit BLACK ICE")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('1'):
            stdscr.addstr(7, 2, "[+] Monitoring Traffic...")
            stdscr.refresh()
            start_sniffing()
        elif key == ord('2'):
            stdscr.clear()
            with open(SCAN_LOG, "r") as log:
                lines = log.readlines()  # Fixed: added parentheses
                for idx, line in enumerate(lines[-10:]):
                    stdscr.addstr(idx + 2, 2, line.strip())
            stdscr.refresh()
            stdscr.getch()
        elif key == ord('3'):
            break

# Start Sniffer
def start_sniffing(interface="eth0"):
    scapy.sniff(iface=interface, store=False, prn=detect_port_scan)

# Execute interactive menu
if __name__ == "__main__":
    curses.wrapper(menu)

