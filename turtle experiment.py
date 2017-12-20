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

draw_star(200, -300, 60, 200, "white", "purple")
draw_star(-350, 200, 60, 200, "white", "purple")



justin.shape("turtle")
justin.color("white")


justin.home()
justin.penup()
justin.setx(150)
justin.sety(-100)
justin.pendown()
justin.begin_fill()
justin.circle(120)
justin.end_fill()
justin.penup()
justin.setx(-150)
justin.pendown()
justin.begin_fill()
justin.circle(120)
justin.end_fill()
justin.penup()
justin.home()
justin.pendown()
justin.pencolor("green")
justin.begin_fill()
justin.circle(120)
justin.end_fill
justin.begin_fill()
justin.circle(120)
justin.end_fill()
justin.begin_fill()
justin.circle(-120)
justin.end_fill()
justin.color("yellow")
justin.pencolor("green")
justin.begin_fill()
justin.circle(80)
justin.end_fill()
justin.begin_fill()
justin.circle(-80)
justin.end_fill()
justin.color("red")
justin.pencolor("green")
justin.begin_fill()
justin.circle(50)
justin.end_fill()
justin.begin_fill()
justin.circle(-50)
justin.end_fill()
justin.dot(70,"blue")

speed(50)

done()
