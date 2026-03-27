from port_scanner.scanner import scan_ports
from password_checker.checker import check_password
from logger.logger import log_event
from banner import show_banner
from colorama import Fore, init

init()

def main():
    print(Fore.GREEN + "Starting Network Security Toolkit 🚀")
    show_banner()
    
    while True:
        choice = input("""
1. Scan Network Ports
2. Check Password Strength
3. Secret Mode 😎
4. Exit
Choose: """)

        if choice == "1":
            ip = input("Enter Target IP: ")
            print("[+] Scanning started...")
            scan_ports(ip)
            log_event(f"Scanned {ip}")

        elif choice == "2":
            pwd = input("Enter Password: ")
            result = check_password(pwd)
            print(f"Strength: {result}")
            log_event("Password checked")

        elif choice == "3":
            print("Launching Secret Mode...")
            import antigravity

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()