# Banner Grabbing - identify what software is running on open ports
# Used in reconnaissance phase of penetration testing

import socket

def grab_banner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((host, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return "No banner retrieved"

host = input("Enter host: ")
ports = [21, 22, 80, 443]

print(f"\nGrabbing banners from {host}...\n")
for port in ports:
    banner = grab_banner(host, port)
    print(f"Port {port}: {banner}")