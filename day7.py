# Network ping sweeper
# Scans a range of IPs to find live hosts

import subprocess
import platform

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return subprocess.call(command, stdout=subprocess.DEVNULL) == 0

print("Scanning network...\n")
base_ip = "192.168.1."

for i in range(1, 20):
    ip = base_ip + str(i)
    if ping(ip):
        print(f"Host alive: {ip}")