
# ❄️ Black Ice – Network Scan Detection & Prevention 🚀

**Black Ice** is an advanced network security tool built to detect and prevent port scans and reconnaissance attempts. It uses **Scapy** to analyze network traffic in real time and automatically blocks suspicious IP addresses.

---

## 🛠️ Features

- ✅ **Real-Time Detection** – Monitors your network to spot port scan attempts.  
- ✅ **Auto Blocking** – Adds firewall rules (iptables) to block malicious IPs on Linux.  
- ✅ **Interactive Interface** – Uses **curses** for a clean, terminal-based UI.  
- ✅ **Event Logging** – Keeps a log of all blocked IPs for audit purposes.

---

## 📥 Installation

### 🔹 Requirements

- Python 3.8+  
- Linux (Ubuntu, Debian, Kali, etc.)  
- Required packages: `scapy`, `curses`

### 🔹 Install Dependencies

```bash
pip install scapy
sudo apt install python3-curses  # Ensures curses compatibility
```

Then clone the repo:

```bash
git clone https://github.com/hikarii1120/blackice
cd blackice
```

---

## 🚀 Usage

To run Black Ice:

```bash
sudo python3 black_ice.py
```

From the main menu, you can:

- 1️⃣ Start network traffic monitoring  
- 2️⃣ View logs of blocked IPs  
- 3️⃣ Exit the program

---

## ⚠️ Important Notes

- Run **Black Ice** with `sudo` so it can modify firewall rules.  
- Built for **Linux**. On Windows, you'll need an alternative firewall (iptables not supported).  
- You can tweak the detection sensitivity by editing the `THRESHOLD` variable in the code.

---

## 🤝 Contributions

Pull requests, forks, and issue discussions are welcome!  
Feel free to suggest improvements or submit new features.

---

## 📜 License

This project is licensed under the **MIT License**.  
You're free to use and modify it—just give credit to the original authors.
