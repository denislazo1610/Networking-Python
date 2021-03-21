import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    #Accepting clients
    clientsocket, address =  s.accept()
    #It tells you if you have connection with client
    print(f"Connection from {address} has been established!") 

    msg = "WelcomeToTheServer!"
    #Limiting the HEADER less than 10 spaces
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    #Sending message
    clientsocket.send(bytes(msg, "utf-8")) 
    #Finish with Client
    clientsocket.close()
