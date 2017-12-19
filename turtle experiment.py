import random
from turtle import *

bgcolor("black")
justin = Turtle()

def draw_star(x, y, points, size, line, fill):
    angle = 180 - (360 / points)
    
    color(line, fill)
    begin_fill()
    for i in range(points):
        forward(size)
        left(angle)
    end_fill()


justin.shape("turtle")
justin.color("white")


justin.home()
justin.position()
(0.00,0.00)
justin.begin_fill()
justin.begin_fill()
justin.circle(50)
justin.end_fill()
justin.begin_fill()
justin.circle(-50)
justin.end_fill()
justin.pencolor("yellow")
justin.penup()
justin.setpos((120, 0))
justin.pendown()
justin.circle(80)
justin.circle(-80)
justin.penup()
justin.set
justin.circle(120)
justin.circle(-120)
justin.dot(50,"blue")

speed(10)


done()

    
