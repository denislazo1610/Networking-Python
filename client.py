import socket

HEADER = 64 # Video

PORT = 65432        # No cambiar
FORMAT = 'utf-8' # Video
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

