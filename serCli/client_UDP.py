import socket

SERVER_ADDRESS = ("127.0.0.1", 9000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    stringa = input("-> ")
    #stringa.encode() trasforma la stringa in binario
    s.sendto(stringa.encode(), SERVER_ADDRESS)
    if stringa == "EXIT":
        break