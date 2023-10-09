#disegnare 9 poligoni differenti
import turtle

x= 0
y= -100
lung = int(input("inserire il numero: "))
finestra = turtle.Screen()
tarta = turtle.Turtle()
tarta.color("red")
tarta.speed("slow")

for num in range(3,12):
    tarta.penup()
    if(num%3 == 0):
        x = 5 
        y = y + lung*4
    else:
        x = x + lung*4
    tarta.goto(x, y)
    tarta.pendown()
    gradi = 360 / num
    tarta.begin_fill()
    for i in range(0,num):
        tarta.forward(lung)
        tarta.left(gradi)
        tarta.end_fill()

finestra.mainloop() #gestione finestra