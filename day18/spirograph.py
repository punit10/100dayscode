import turtle
from turtle import Turtle, Screen
import random

# Create a turtle object
pen = turtle.Turtle()
turtle.colormode(255)
pen.speed(0)
pen.pensize(1)


def set_color():
    r = random.randint(10,  255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(angle_size):
    for _ in range(int(360 / angle_size)):
        pen.color(set_color())
        pen.circle(100)
        pen.setheading(pen.heading() + angle_size)


draw_spirograph(18)

screen = Screen()
screen.exitonclick()
