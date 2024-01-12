import random
import turtle

def main():
    finestra = turtle.Screen()
    tarta = turtle.Turtle()
    tarta.speed(6)
    time = 0 #conta i minuti
    continua = True
    x=0
    y=0

    listaX = [0]
    listaY = [0]
    
    while(continua == True):
        direzione = random.randint(0,3)
        if direzione == 0:
            y -= 10
        elif direzione == 1:
            y += 10
        elif direzione == 2:
            x += 10
        elif direzione == 3:
            x -= 10

        for i in range(0, time):
            if x == listaX[i] and y == listaY[i]:
                print(f"Bob è già passato per {x, y}")
        
        listaX.append(x)
        listaY.append(y)
        tarta.goto(listaX[time], listaY[time])
        print(listaX , listaY)
        time += 1
        if time == 60:
            time = 0
            x = 0
            y = 0
            listaX[0:60] = [0]
            listaY[0:59] = [0]
            finestra.clearscreen()
            print("azzera")
        if listaX[time] == 100 and listaY[time] == 100:
            continua = False
        finestra.mainloop



if __name__ == "__main__":
    main()