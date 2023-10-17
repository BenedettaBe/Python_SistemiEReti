import turtle
def eseguiComandi(lista):
    finestra = turtle.Screen()
    tarta = turtle.Turtle()
    tarta.speed("slow")#velocità della turtle
    for comando in lista:
        if(comando == "D"):
            tarta.right(90)
        elif(comando == "S"):
            tarta.left(90)
        elif(comando == "A"):
            tarta.forward(100)
    finestra.mainloop

def main():
    comandi = []
    comandiPossibili = ["A", "D", "S"]
    com = "A"
    while com in comandiPossibili:
        com = input("scrivere comando: ")
        comandi.append(com)
    
    eseguiComandi(comandi)


if __name__ == "__main__":
    main()