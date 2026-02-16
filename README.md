Shadow AI Hunter (Community Edition)

(Place your generated banner image here)

Identify Unauthorized "Shadow AI" Agents in Your Enterprise Network.

As AI adoption accelerates, developers and employees are deploying autonomous agents (like OpenClaw/Moltbot) on corporate infrastructure without IT oversight. These "Shadow AI" instances often run on default ports with insecure configurations, creating massive data exfiltration risks.

Shadow AI Hunter is a lightweight, open-source reconnaissance tool designed to detect these silent risks before they become breaches.

🚀 Capabilities (v1.0)

Zero-Dependency Scanning: Written in pure Python. No external binaries (like Nmap) required.

Targeted Detection: Specifically hunts for TCP Port 18789 (The default OpenClaw/Moltbot signature).

Multi-Threaded Engine: Scans /24 subnets in seconds.

Audit Ready: Generates clear console output for immediate reporting.

📦 Installation

Prerequisites

Python 3.6+

Network access to the target subnet

Setup

Clone the repository:

git clone [https://github.com/Move78-International/shadow-ai-hunter.git](https://github.com/Move78-International/shadow-ai-hunter.git)
cd shadow-ai-hunter


Install dependencies (Optional, only for color output in future versions):

pip install -r requirements.txt


⚔️ Usage

Syntax:

python src/shadow_hunter.py <TARGET_IP_OR_CIDR>


Example - Scan a local subnet:

python src/shadow_hunter.py 192.168.1.0/24


Example Output:

[*] Starting scan on network: 192.168.1.0/24
[*] Target Port: 18789
[*] Threads: 50
------------------------------------------------------------
[+] FOUND POTENTIAL AGENT: 192.168.1.105:18789
[+] FOUND POTENTIAL AGENT: 192.168.1.112:18789
------------------------------------------------------------
[*] Scan Complete.
[*] Total Agents Found: 2


⚠️ Legal Disclaimer

Please read carefully before using.

This software is provided for educational and defensive audit purposes only.

Do not scan networks you do not own.

Do not scan networks without explicit written permission.

Scanning unauthorized networks may violate the Computer Fraud and Abuse Act (CFAA) in the US, the Cybersecurity Law of the PRC in China, and other applicable local laws.

Move78 International accepts no responsibility for unauthorized use of this tool.

🗺️ Roadmap

v1.0: Network Port Scanner (Current)

v2.0: Agent-Based Host Scanner (Local process & file system audit)

v3.0: "Sentinel" Real-time Prevention & Kill-Switch

🤝 Contributing

We welcome contributions! Please see CONTRIBUTING.md (coming soon) for details on how to submit pull requests.

📄 License

Distributed under the MIT License. See LICENSE for more information.

Maintained by Move78 International Securing the AI Era.