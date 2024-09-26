from threading import Thread
import time
import socket
MY_ADDRESS = ("127.0.0.1", 9000) #assegno ip e porta al processo
BUFFER_SIZE = 4096 #byte
SERVER_ADDRESS = ("192.168.1.112", 9000)

class MioThread(Thread):
    def __init__(self,s):
        super().__init__()
        self.s = s 
    def run(self):
        #codice del thread
        while True:
            data, sender_address = self.s.recvfrom(BUFFER_SIZE) #serve spazio di memoria in byte, ritorna dati + indirizzo
            stringa = data.decode() #devo castare data perchè arriva in binary
            print(f"Ricevuto {stringa} da {sender_address}")
            if stringa == "EXIT":
                break
    def kill(self):
        self.running = False
            
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    thread=MioThread(s)
    partito = True
    while True:
        string = input("-> ")
        binary_string = string.encode()
        s.sendto(binary_string, SERVER_ADDRESS)
        if partito:
            thread.start()
            partito = False
            
if __name__ == "__main__":
    main()