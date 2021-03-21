import socket
import threading

#C:\Users\enriq\OneDrive\Desktop\Git\Networking Python  (This is to use the command prompt)

HEADER = 64 # Video

PORT = 65432        # No cambiar
SERVER = socket.gethostbyname(socket.gethostname()) # No cambiar HOST

ADDR = (SERVER, PORT) # Video
FORMAT = 'utf-8' # Video
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Video
print("Socket created")

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

#Encoding message
def sendTextViaSocket(message, sock):
    # encode the text message
    encodedMessage = bytes(message, 'utf-8')

    # send the data via the socket to the server
    sock.sendall(encodedMessage)

    # receive acknowledgment from the server
    encodedAckText = sock.recv(1024)
    ackText = encodedAckText.decode('utf-8')

    # log if acknowledgment was successful
    if ackText == "text_received":
        print('server acknowledged reception of text')
    else:
        print('error: server has sent back ' + ackText)
    # end if
# end function

def start(): # Server starts Running
    server.listen()
    print("[LISTENING] Server is listening") #This is testing
    while True:

        conn, addr = server.accept() #Connection with the clients
        print("Got connection from", addr)
        #conn.send("Thank you for connecting") #JUST TESTING
        print(conn.recv(1024)) #print message from client

        #conn.send('Thank you for connecting') NOT WORKING
        conn.close() #Connection close

        '''
        thread = threading.Thread(target= handle_client, args =(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        '''

print("[STARTING] server is starting ...")
start()