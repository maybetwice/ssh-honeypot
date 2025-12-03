import socket
from config import HOST, PORT, BANNER, DENY_MESSAGE
from logger import log

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[+] Honeypot running on port {PORT}...")

    while True:
        conn, addr = server.accept()
        ip = addr[0]
        log(f"Connection from {ip}")

        conn.send(BANNER)
        try:
            data = conn.recv(1024)
            if data:
                log(f"Received data from {ip}: {data.decode(errors='ignore')}")
        except Exception as e:
            log(f"Error reading from {ip}: {e}")

        conn.send(DENY_MESSAGE)
        conn.close()

if __name__ == "__main__":
    start_honeypot()
