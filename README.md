❄️ Black Ice - Detección y Prevención de Escaneos de Red 🚀
❄️ Black Ice - Detección y Prevención de Escaneos de Red 🚀

Black Ice es una herramienta avanzada de seguridad en redes diseñada para detectar y prevenir escaneos de puertos y posibles ataques de reconocimiento. Utiliza scapy para analizar el tráfico de red en tiempo real y bloquea automáticamente las IPs sospechosas.

🛠️ Características

✅ Detección en Tiempo Real: Monitorea la red y detecta intentos de escaneo de puertos.✅ Bloqueo Automático: Añade reglas a iptables (Linux) para bloquear IPs maliciosas.✅ Interfaz Interactiva: Utiliza curses para una experiencia visual atractiva.✅ Registro de Eventos: Guarda un log con las IPs bloqueadas para auditoría.

📥 Instalación

🔹 Requisitos

Python 3.8+

Linux (Ubuntu, Debian, Kali, etc.)

Paquetes necesarios: scapy, curses

🔹 Instalación de Dependencias

Ejecuta los siguientes comandos:

pip install scapy
sudo apt install python3-curses  # Para asegurar compatibilidad con curses

Clona este repositorio:

git clone https://github.com/tuusuario/black-ice.git
cd black-ice

🚀 Uso

Para ejecutar Black Ice, usa:

sudo python3 black_ice.py

Desde el menú, puedes:
1️⃣ Iniciar monitoreo de tráfico en la red.2️⃣ Revisar logs de IPs bloqueadas.3️⃣ Salir del programa.

⚠️ Notas Importantes

Ejecuta Black Ice como administrador (sudo) para que pueda modificar reglas de firewall.

Funciona en Linux. Para Windows, es necesario un firewall alternativo en lugar de iptables.

Puedes ajustar el umbral de detección modificando THRESHOLD en el código.

🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes hacer un fork, proponer cambios en issues, o enviar un pull request.

📜 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente, pero siempre dando crédito a los autores originales.
