#memoriazzare in una lista i comandi della turtle chiesti da tastiera e dopo eseguirli
import turtle

def nord(turtle):
    turtle.setheading(90)
    turtle.forward(100)

def sud(turtle):
    turtle.setheading(270)
    turtle.forward(100)

def ovest(turtle):
    turtle.setheading(180)
    turtle.forward(100)

def est(turtle):
    turtle.setheading(0)
    turtle.forward(100)

def main():
    
    dizionario = {"N": nord, "S":sud, "E":est, "O": ovest}
    movimento = input("scrivi N per somma, S per prodotto, E per sottrazione, O per divisone  : ")
    finestra = turtle.Screen()
    tarta = turtle.Turtle()
    tarta.speed("slow")
    while True:
        if movimento in dizionario:
            movimento = input("scrivi N per somma, S per prodotto, E per sottrazione, O per divisone  : ")    
            dizionario[movimento](tarta)
            finestra.mainloop
        else:
            exit(1)


if __name__ == "__main__":
    main()