import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        mess = input("(comando|size)-> ")

        #com = input("Inserisci il comando: \n->")
        #size = input ("Inserisci lo spostamento/angolo: \n->")
        #mex = f"{com}|{size}" # com+"|"+size java stile
        
        if mess == "EXIT":
            break
        s.sendto(mess.encode(), SERVER_ADDRESS)
        

        mex, _ = s.recvfrom(BUFFER_SIZE)
        print(mex.decode())
        
    s.close()

if __name__ == '__main__':
    main()