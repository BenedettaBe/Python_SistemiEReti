import socket

MY_ADDRESS = ("127.0.0.1", 8090)
BUFFER_SIZE = 4096 #byte

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(MY_ADDRESS)
while True:
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    stringa = data.decode()
    print(f"Ricevuto {stringa} da {sender_address}")
    if stringa == "EXIT":
        break