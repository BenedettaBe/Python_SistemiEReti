import socket

SERVER_ADDRESS = ("127.0.0.1", 8090)
BUFFER_SIZE = 4096 #byte

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    stringa = input("-> ")
    #stringa.encode() trasforma la stringa in binario
    s.sendto(stringa.encode(), SERVER_ADDRESS)
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    stringa = data.decode()
    print(f"Ricevuto {stringa} da {sender_address}")
    if stringa == "EXIT":
        break