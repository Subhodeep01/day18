from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
turtle.speed(0)
turtle.pensize(2)
turtle.shape("turtle")
turtle.color("Blue")

colormode(255)


def random_col():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col = (r, g, b)
    return col


def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        colors = random_col()
        turtle.pencolor(colors)
        ini_heading = turtle.heading()
        turtle.setheading(ini_heading + size_of_gap)
        turtle.circle(100)


spirograph(5)
# colors = ["Red", "Green", "Yellow", "Orange", "Blue", "Violet", "Magenta", "Lime", "Indigo", "HotPink", "DarkGreen",
#           "DeepSkyBlue", "SlateGray", "DarkOrange", "SlateBlue", "MidnightBlue"]
# for i in range(20):
#     turtle.forward(150)
#     turtle.left(90)
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()
# c = 0
# for n in range(3, 11):
#     turtle.color(colors[c])
#     i = 360 / n
#     for t in range(n):
#         turtle.forward(80)
#         turtle.left(i)
#     c += 1
# for i in range(201):
#     colors = random_col()
#     direction = random.choice([0, 90, 180, 270])
#     turtle.pencolor(colors)
#     turtle.setheading(direction)
#     turtle.forward(20)

screen = Screen()

screen.exitonclick()
