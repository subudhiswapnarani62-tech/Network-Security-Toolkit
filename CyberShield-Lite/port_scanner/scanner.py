import socket

# Port Scanner Module
def scan_ports(host):
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8000, 8080] # Common ports
    print(f"Scanning common ports on {host}...")
    
    found = False
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                # connect_ex returns 0 if the connection is successful
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"[!] Port {port} is OPEN")
                    found = True
        except Exception:
            # Silently ignore errors for specific ports and continue
            continue
            
    if not found:
        print("[-] No common open ports found.")
    print("Scanning complete.")
