#disegnare una stella a n punte con n chiesto da tastiera
import turtle

n = int(input("inserire il numero di punte: "))
lung = 60
finestra = turtle.Screen()
tarta = turtle.Turtle()
tarta.color("red")
tarta.speed("slow")

gradi = 180 / n
tarta.begin_fill()
for i in range(0,n):
   if(n % 2 != 0):  
       tarta.forward(lung)
       tarta.right(180-gradi)

tarta.end_fill()

finestra.mainloop() #gestione finestra