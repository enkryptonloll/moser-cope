# MOSERSCAPE v3.0
### RAT Generator + OSINT + DDOS + Exploitation Toolkit
#### Created by: @shuukaid on tg

---

## SCREENSHOT

![MOSERSCAPE Menu](screenshot.png)

---

## INSTALLATION

```
pip install -r requirements.txt
python3 moserscape.py

requirements.txt

requests
colorama
beautifulsoup4
dnspython
phonenumbers
python-whois
paramiko
scapy
cryptography
pillow
pyautogui
psutil
pynput
opencv-python
numpy

<details> <summary><strong>📁 OSINT MODULE (Options 1-15)</strong></summary>
#	Tool	Description
1	Google Dork	Generate Google search queries
2	Username Lookup	Search 50+ platforms for username
3	Email Lookup	MX records, Gravatar, breach check
4	Phone Lookup	Country, carrier, timezone info
5	IP Lookup	Geolocation, ISP, proxy detection
6	DNS Lookup	A, MX, NS, TXT records
7	Port Scanner	Multi-threaded TCP scan
8	Subdomain Enum	Discover subdomains
9	WHOIS Lookup	Domain registration info
10	Pastebin Search	Find pastes by query
11	Reverse Image	Google reverse image search
12	Metadata Extract	EXIF data from images
13	Breach Check	Check email in data breaches
14	Wayback Machine	Archived website versions
15	Social Search	Generate social media URLs
</details><details> <summary><strong>📁 DDOS ATTACKS (Options 16-20)</strong></summary>
#	Attack	Description
16	HTTP Flood	Layer 7 HTTP GET/POST flood
17	SYN Flood	TCP SYN packet flood
18	UDP Flood	UDP packet flood
19	ICMP Flood	Ping flood
20	Slowloris	Slow HTTP connection attack
</details><details> <summary><strong>📁 PAYLOAD GENERATOR (Options 21-30)</strong></summary>
#	Payload	Description
21	Full RAT	Complete RAT with all features
22	Persistence	Survive reboots (startup/crontab)
23	Keylogger	Capture keystrokes
24	Stealer	Steal passwords, files, WiFi
25	Reverse Shell	Connect back to listener
26	Bind Shell	Listen for connections
27	Add Webhook	Add Discord/Telegram webhook
28	Clear Webhooks	Remove all webhooks
29	Show Webhooks	List current webhooks
</details><details> <summary><strong>📁 EXPLOIT MODULE (Options 31-36)</strong></summary>
#	Tool	Description
31	FTP Bruteforce	Try FTP login with wordlist
32	SSH Bruteforce	Try SSH login with wordlist
33	SQLi Scanner	Test for SQL injection
34	XSS Scanner	Test for XSS vulnerabilities
35	Dir Buster	Discover hidden directories
36	WordPress Scan	Detect WordPress components
</details><details> <summary><strong>📁 SYSTEM MODULE (Options 41-50)</strong></summary>
#	Tool	Description
41	List Processes	View running processes
42	Kill Process	Terminate process by PID
43	Net Connections	View network connections
44	Disk Usage	Check disk space
45	Sensors	Temperature sensors
46	Battery Info	Battery percentage/status
47	Screenshot	Capture desktop
48	Webcam	Capture from webcam
49	System Info	Hostname, OS, user, IPs
50	WiFi Passwords	Extract saved WiFi passwords
</details><details> <summary><strong>📁 NETWORK/CRYPTO (Options 51-55)</strong></summary>
#	Tool	Description
51	Packet Sniffer	Capture network packets
52	ARP Scan	Discover live hosts on network
53	Traceroute	Trace route to target
54	Generate Key	Create Fernet encryption key
55	Encrypt/Decrypt	File encryption utilities
</details>
QUICK START

    Install: pip install -r requirements.txt

    Run: python3 moserscape.py

    Select a number and follow prompts

    For payloads: Add webhook first (option 27)

    For bruteforce: Create users.txt and pass.txt

COMMANDS
Command	Section
1-15	OSINT tools
16-20	DDOS attacks
21-30	Payload generator
31-36	Exploitation
41-50	System tools
51-55	Network/Crypto
0	Exit
DISCLAIMER

For educational/authorized testing only. Illegal use is on you.
CONTACT

Telegram: @shuukaid
VERSION

v3.0 - All modules included
