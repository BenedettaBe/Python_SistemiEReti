#creare un server TCP che permette la connessione a un client alla volta e mette in coda gli altri
#il client rimane connesso per 30 secondi circa
#il client manda la richiesta con il nome e il server controlla che non sia già connesso
import socket
import threading
import time
import turtle
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

            
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)

    tarta = turtle.Turtle()
    finestra = turtle.Screen()

    while True:
        message, address = s.recvfrom(BUFFER_SIZE)
        message = message.decode()
        comando, size = message.split("|")
        
        if(comando == "avanti"):
            tarta.forward(int(size))
            s.sendto("comando avanti eseguito".encode(), address)

        elif(comando == "indietro"):
            tarta.backward(int(size))
            s.sendto("comando indietro eseguito".encode(), address)

        elif(comando == "destra"):
            tarta.right(int(size))
            s.sendto("comando destra eseguito".encode(), address)

        elif(comando == "sinistra"):
            tarta.left(int(size))
            s.sendto("comando sinistra eseguito".encode(), address)
        
        else:
            s.sendto("comando non accettato".encode(), address)

        """
        movements = {"forward": victor.forward, 
                    "backward": victor.backward,
                    "left": victor.left,
                    "right": victor.right}
        if com in movements:
            movements[com](int(size))#compatto i comandi con questa sintassi
            s.sendto(f"comando {com} eseguito con successo".encode(), address)
        else:
            print("comando non riconosciuto")
            s.sendto(f"comando {com} non riconosciuto".encode(), address)
            
        """
    s.close()

if __name__ == '__main__':
    main()