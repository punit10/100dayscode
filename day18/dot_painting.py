import turtle
from turtle import Turtle, Screen
import random

# Create a turtle object
pen = turtle.Turtle()
turtle.colormode(255)
pen.speed(0)
pen.pensize(1)
pen.penup()
pen.hideturtle()


def set_color():
    r = random.randint(10,  255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


x_cord, y_cord = -250, -200
dots_in_row = 10
for j in range(0, dots_in_row):
    for i in range(0, dots_in_row):
        pen.goto(x_cord + (i*50), y_cord + (j*50))
        pen.dot(30, set_color())

screen = Screen()
screen.exitonclick()
