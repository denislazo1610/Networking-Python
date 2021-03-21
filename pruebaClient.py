import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 1234))

while True:

#We will create a message 
    full_msg = ''
    new_msg = True
    while True:
        #Receice Message
        msg = s.recv(16)

        #If the lenght of the message is 0 or less than that then it is
        #going to break the while
        #if len(msg) <= 0:
            #break
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
   

        #if the mesage is not equal to 0 then it is going to add to full_msg
        full_msg += msg.decode("utf-8")
        print(full_msg)
        '''
        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            #FOR FUTURE MESSAGES
            full_msg = ''
        '''

    #Print message
    print(full_msg)