import socket
import threading

HEADER = 64 
PORT = 5050
SERVER = "10.50.100.248"

#Another way to do this is
#SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
       msg_length = conn.recv(HEADER).decode()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target= handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting")
start()

'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(F"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
'''
