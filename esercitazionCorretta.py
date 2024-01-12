import random
import turtle

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    finestra = turtle.Screen()
    tarta = turtle.Turtle()
    percorso = {0: Punto(0,0)}
    for tempo in range(1,60):
        direzione = random.randint(0,3)
        #simulare movimenti casuali
        if direzione == 0:
            percorso[tempo] = Punto(percorso[tempo-1].x, percorso[tempo-1].y - 10)
        elif direzione == 1:
            percorso[tempo]= Punto(percorso[tempo-1].x, percorso[tempo-1].y + 10)
        elif direzione == 2:
            percorso[tempo]= Punto(percorso[tempo-1].x + 10, percorso[tempo-1].y)
        elif direzione == 3:
            percorso[tempo]= Punto(percorso[tempo-1].x - 10, percorso[tempo-1].y)

        #disegnare percorso con turtle        
        tarta.goto(percorso[tempo].x, percorso[tempo].y)

        # BONUS controllo passaggio punto già visitato
        for minuto in range(0, tempo):
            if (percorso[tempo].x == percorso[minuto].x) and (percorso[tempo].y == percorso[minuto].y):
                print(f"Bob è già passato per {percorso[tempo].x}, {percorso[tempo].y}")

    #scrittura su file 
        #COLONNE: minuto, x,y
    with open("percorso.csv", "w") as file:
        file.write(f"minuto, posx, posy \n")
        #ciclo sul dizionario percorso
        for minuto in percorso:
           posx = percorso[minuto].x
           posy = percorso[minuto].y
           file.write(f"{minuto}, {posx}, {posy} \n")
    finestra.mainloop()

if __name__ == "__main__":
    main()