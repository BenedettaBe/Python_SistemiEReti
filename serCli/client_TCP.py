import socket
SERVER_ADDRESS = ("192.168.1.112", 9090)
BUFFER_SIZE = 4096


def main():
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    s.sendall("messaggio dal client".encode())
    message = s.recv(BUFFER_SIZE)
    print(f"Ricevuto <{message.decode()}> dal server")

    s.close

if __name__ == "__main__":
    main()