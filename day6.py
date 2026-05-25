# System Reconnaissance Tool
# Gathers information about the local system
# Used in security audits

import os
import socket
import platform

def system_recon():
    print("=" * 50)
    print("SYSTEM RECONNAISSANCE REPORT")
    print("=" * 50)

    print(f"\nHostname:        {socket.gethostname()}")
    print(f"IP Address:      {socket.gethostbyname(socket.gethostname())}")
    print(f"OS:              {platform.system()}")
    print(f"OS Version:      {platform.version()}")
    print(f"Architecture:    {platform.machine()}")
    print(f"Processor:       {platform.processor()}")

    print("\n--- Running Processes ---")
    processes = os.popen("tasklist").read()
    print(processes[:500])

system_recon()