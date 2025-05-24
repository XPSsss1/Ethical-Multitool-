import os
import sys
import hashlib
import requests
import socket
import platform
import time
import random

# Banner
def display_banner():
    banner = """▒██   ██▒ ██▓███    ██████ 
▒▒ █ █ ▒░▓██░  ██▒▒██    ▒ 
░░  █   ░▓██░ ██▓▒░ ▓██▄   
 ░ █ █ ▒ ▒██▄█▓▒ ▒  ▒   ██▒
▒██▒ ▒██▒▒██▒ ░  ░▒██████▒▒
▒▒ ░ ░▓ ░▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░
░░   ░▒ ░░▒ ░     ░ ░▒  ░ ░
 ░    ░  ░░       ░  ░  ░  
 ░    ░                 ░  
"""
    print(banner)

# ---- OSINT Tools ----
def username_checker():
    print("[+] Checking username across platforms (stub)")

def email_breach_checker():
    print("[+] Checking email breach status (stub)")

def phone_lookup():
    print("[+] Looking up phone number info (stub)")

def metadata_extractor():
    print("[+] Extracting metadata from file (stub)")

# ---- Networking ----
def port_scanner():
    print("[+] Running advanced port scanner (stub)")

def traceroute():
    print("[+] Performing traceroute (stub)")

def subnet_calculator():
    print("[+] Calculating subnet (stub)")

def ping_flood():
    print("[+] Sending ping flood (stub)")

# ---- Brute Forcers ----
def zip_brute():
    print("[+] Brute-forcing ZIP file password (stub)")

def ftp_brute():
    print("[+] Brute-forcing FTP credentials (stub)")

def pdf_crack():
    print("[+] Cracking PDF password (stub)")

def web_login_brute():
    print("[+] Brute-forcing login form (stub)")

# ---- System Tools ----
def system_info():
    print("[+] Gathering system info...")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU: {platform.processor()}")
    print(f"Hostname: {socket.gethostname()}")

def network_monitor():
    print("[+] Monitoring network adapters (stub)")

def wifi_passwords():
    print("[+] Dumping WiFi passwords (stub - Windows only)")

# ---- Web Tools ----
def url_revealer():
    print("[+] Revealing short URL (stub)")

def tech_analyzer():
    print("[+] Analyzing website technologies (stub)")

def fake_login_page():
    print("[+] Launching fake login page (HTML only - stub)")

# ---- File Tools ----
def virustotal_checker():
    print("[+] Checking hash on VirusTotal (stub)")

def hash_generator():
    string = input("Enter string to hash: ")
    print(f"MD5: {hashlib.md5(string.encode()).hexdigest()}")
    print(f"SHA1: {hashlib.sha1(string.encode()).hexdigest()}")
    print(f"SHA256: {hashlib.sha256(string.encode()).hexdigest()}")

def filetype_identifier():
    print("[+] Identifying file type (stub)")

# ---- Fun Tools ----
def anonymous_mode():
    print("[+] Activating anonymous mode... [prank]")
    time.sleep(1)
    print("🕶️ You are now anonymous.")

def matrix_terminal():
    print("[+] Launching Matrix mode (stub)")

def fake_ransomware():
    print("[!] Simulating ransomware (just a prank!)")

def system_hack_prank():
    print("[!] System breach detected! (fake)")

# ---- Intelligence ----
def fake_identity():
    print("[+] Generating fake identity (stub)")

def crypto_price():
    print("[+] Fetching crypto price (stub)")

# ---- Menu ----
def main_menu():
    while True:
        display_banner()
        print("""
[1] OSINT Tools
[2] Networking
[3] Brute Forcers
[4] System Tools
[5] Web Tools
[6] File Tools
[7] Fun / Pranks
[8] Intelligence
[0] Exit
        """)
        choice = input(">> ")

        if choice == "1":
            username_checker(); email_breach_checker(); phone_lookup(); metadata_extractor()
        elif choice == "2":
            port_scanner(); traceroute(); subnet_calculator(); ping_flood()
        elif choice == "3":
            zip_brute(); ftp_brute(); pdf_crack(); web_login_brute()
        elif choice == "4":
            system_info(); network_monitor(); wifi_passwords()
        elif choice == "5":
            url_revealer(); tech_analyzer(); fake_login_page()
        elif choice == "6":
            virustotal_checker(); hash_generator(); filetype_identifier()
        elif choice == "7":
            anonymous_mode(); matrix_terminal(); fake_ransomware(); system_hack_prank()
        elif choice == "8":
            fake_identity(); crypto_price()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")
        input("\nPress Enter to continue...\n")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main_menu()
