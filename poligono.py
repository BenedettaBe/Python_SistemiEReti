import turtle #esempio di importazione di un modulo built-in

num = int(input("inserire il numero: "))
lung = int(input("inserire il numero: "))
gradi = 360 / num
finestra = turtle.Screen()
tarta = turtle.Turtle()
tarta.color("red")
tarta.speed("slow")

tarta.begin_fill()
for i in range(0,num):
    tarta.forward(lung)
    tarta.left(gradi)

tarta.end_fill()
finestra.mainloop() #gestione finestra
