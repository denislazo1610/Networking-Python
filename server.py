import socket
import threading

#C:\Users\enriq\OneDrive\Desktop\Git\Networking Python  (This is to use the command prompt)

HEADER = 64 # Video

PORT = 65432        # No cambiar
SERVER = "10.50.100.248" # No cambiar HOST

ADDR = (SERVER, PORT) # Video
FORMAT = 'utf-8' # Video
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Video
server.bind(ADDR) # Video

'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
'''

def handle_client(conn, addr): #Deal with clients
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False


        print(f"[{addr}] {msg}")

    conn.close()

def start(): # Server starts Running
    server.listen(2)
    print("[LISTENING] Server is listening on") #This is testing
    while True:
        conn, addr = server.accept() #Connection with the clients
        print("Got connection from", addr)
        #conn.send('Thank you for connecting') NOT WORKING
        conn.close() #Connection close

        '''
        thread = threading.Thread(target= handle_client, args =(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        '''

print("[STARTING] server is starting ...")
start()