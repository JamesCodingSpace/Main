import turtle
import math

def kreis_aus_dreiecken(radius, anzahl_dreiecke):
    for x in range(3):
        window = turtle.Screen()
        window.bgcolor("white")
        
        pen = turtle.Turtle()
        pen.speed(200)

        winkel = 360 / anzahl_dreiecke

        for _ in range(anzahl_dreiecke):
            dreieck_seite = 2 * radius * math.sin(math.radians(winkel / 2))
            for _ in range(3):
                pen.forward(dreieck_seite)
                pen.left(120)
            pen.left(winkel)
        
        pen = turtle.Turtle()
        pen.speed(1000)

        winkel = 360 / (anzahl_dreiecke*2)

        for _ in range(anzahl_dreiecke*2):
            dreieck_seite = 16 * radius * math.sin(math.radians(winkel / 2))
            for _ in range(3):
                pen.forward(dreieck_seite)
                pen.left(120)
            pen.left(winkel)

        for l in range(100):
            for _ in range(anzahl_dreiecke):
                pen.forward((radius * 3.1415 / anzahl_dreiecke / 10)  (1 / (l + 1)))
                pen.left(360 / anzahl_dreiecke)

        window.exitonclick()

# Kreis aus X gleichseitigen Dreiecken mit Radius Y
kreis_aus_dreiecken(4000, 180)
