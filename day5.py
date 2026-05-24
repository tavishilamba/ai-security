# Port Scanner - basic network reconnaissance tool
# Used by security engineers to find open ports

import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        return False
    except:
        return False

def scan_host(host, start_port, end_port):
    print(f"\nScanning {host} from port {start_port} to {end_port}...")
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"Port {port} is OPEN")
            open_ports.append(port)

    if not open_ports:
        print("No open ports found")
    else:
        print(f"\n{len(open_ports)} open ports found")

host = input("Enter host to scan (try 'scanme.nmap.org'): ")
scan_host(host, 1, 100)