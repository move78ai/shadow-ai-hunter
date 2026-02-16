import socket
import argparse
import ipaddress
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import sys

# --- CONFIGURATION ---
DEFAULT_PORT = 18789  # Default OpenClaw/Moltbot port
TIMEOUT = 1.0         # Socket timeout in seconds
MAX_THREADS = 50      # Concurrency level

# --- BANNER & DISCLAIMER ---
BANNER = """
========================================================================
   _____ _    _          _____   _____  __          __   _    _ 
  / ____| |  | |   /\   |  __ \ / _ \ \ \        / /  | |  | |
 | (___ | |__| |  /  \  | |  | | | | \ \  /\  / /   | |__| |
  \___ \|  __  | / /\ \ | |  | | | | |\ \/  \/ /    |  __  |
  ____) | |  | |/ ____ \| |__| | |_| | \  /\  /     | |  | |
 |_____/|_|  |_/_/    \_\_____/ \___/   \/  \/      |_|  |_|
                                                            
             SHADOW AI HUNTER - v1.0 (Community Edition)             
             Move78 International | Open Source Security             
========================================================================
"""

DISCLAIMER = """
[!] LEGAL DISCLAIMER:
This tool is for educational and defensive purposes only. 
Scanning networks without explicit permission is ILLEGAL and may violate 
local, state, and international laws (including CFAA in the USA and 
Cybersecurity Law in China). 

By running this script, you accept full responsibility for your actions. 
The authors assume no liability for misuse.
========================================================================
"""

def check_port(ip, port):
    """
    Checks if a specific port is open on a target IP.
    Returns the IP if open, None otherwise.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            result = s.connect_ex((str(ip), port))
            if result == 0:
                return str(ip)
    except Exception:
        pass
    return None

def scan_network(cidr_range):
    """
    Scans a CIDR range for the OpenClaw port using threading.
    """
    print(f"[*] Starting scan on network: {cidr_range}")
    print(f"[*] Target Port: {DEFAULT_PORT}")
    print(f"[*] Threads: {MAX_THREADS}")
    print("-" * 60)

    try:
        network = ipaddress.ip_network(cidr_range, strict=False)
    except ValueError:
        print(f"[!] Invalid Network CIDR: {cidr_range}")
        sys.exit(1)

    found_agents = []
    
    # We skip the network and broadcast address for standard /24s, 
    # but iterating all is safer for general logic.
    hosts = list(network.hosts())
    total_hosts = len(hosts)
    print(f"[*] Scanning {total_hosts} hosts... (This may take a moment)")

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {executor.submit(check_port, ip, DEFAULT_PORT): ip for ip in hosts}
        
        for future in futures:
            result = future.result()
            if result:
                print(f"[+] FOUND POTENTIAL AGENT: {result}:{DEFAULT_PORT}")
                found_agents.append(result)

    print("-" * 60)
    print(f"[*] Scan Complete.")
    print(f"[*] Total Agents Found: {len(found_agents)}")
    
    if found_agents:
        print("\n[!] ALERT: The following hosts have port 18789 open.")
        print("[!] Immediate Action Required: Verify if these are authorized AI agents.")
        for agent in found_agents:
            print(f"    -> {agent}")
    else:
        print("\n[ok] No active agents detected on port 18789 in this range.")

def main():
    print(BANNER)
    print(DISCLAIMER)
    
    parser = argparse.ArgumentParser(description="Scan network for unauthorized OpenClaw/Moltbot AI agents.")
    parser.add_argument("target", help="Target IP or CIDR range (e.g., 192.168.1.0/24)")
    args = parser.parse_args()

    # Simple confirmation check
    confirm = input("[?] Do you have permission to scan this target? (y/n): ").lower()
    if confirm != 'y':
        print("[-] Scan aborted by user.")
        sys.exit(0)

    start_time = datetime.now()
    scan_network(args.target)
    end_time = datetime.now()
    print(f"\n[*] Duration: {end_time - start_time}")

if __name__ == "__main__":
    main()