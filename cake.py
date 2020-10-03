import turtle
import random


def two():
    turtle.penup()
    turtle.goto(-40, -50)
    turtle.pendown()
    turtle.right(90)
    for i in range(2):
        turtle.fd(10)
        turtle.right(90)
    for i in range(2):
        turtle.fd(10)
        turtle.left(90)
    turtle.fd(10)


def three():
    turtle.penup()
    turtle.goto(-20, -50)
    turtle.pendown()
    for i in range(2):
        turtle.fd(10)
        turtle.right(90)
    turtle.fd(10)
    turtle.left(180)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    for i in range(2):
        turtle.right(90)
        turtle.fd(10)


# sets background
bg = turtle.Screen()
bg.bgcolor("black")

# Bottom Line 1
turtle.penup()
turtle.goto(-170, -180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160, -150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150, -120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-100, -100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-90, 0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60, 0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30, 0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0, 0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30, 0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)


two()
three()

# Happy Birthday message
turtle.penup()
turtle.goto(-150, 50)
turtle.color("pink")
turtle.pendown()
turtle.write("Happy Birthday!", False,
             align="center", font=("Arial", 24, 'normal', 'bold', 'italic'))
turtle.color("black")


turtle.penup()
turtle.goto(120, 50)
turtle.pendown()
turtle.speed(30)
for i in range(6):
    for colors in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colors)
        turtle.circle(30)
        turtle.left(10)


turtle.done()
