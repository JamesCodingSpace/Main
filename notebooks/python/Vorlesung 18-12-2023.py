import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")

def sqrfunc(Anzahl, Seiten, Laenge):
    for i in range(Anzahl):
        for x in range (Seiten):
            skk.fd(x * Laenge * (i + 1))
            skk.left(90)
    wn.exitonclick()        

sqrfunc(5, 12, 8)            