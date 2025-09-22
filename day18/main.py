import turtle
from turtle import Turtle, Screen


timmy = Turtle()

timmy.shape("turtle")
# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)



for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


# for steps in range(10):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps*10)
#         timmy.right(30)
# timmy.forward(100)

# timmy = Turtle()
# for i in range(3, 10):
#     for j in range(i):
#         color = ('blue', 'red', 'green')
#         timmy.color(color[i % len(color)])
#         timmy.forward(60)
#         timmy.left(360/i)


timmy = Turtle()
def draw_shape(side):
    angle = 360/side
    for _ in range(side):
        timmy.forward(60)
        timmy.right(angle)


no_of_sides = 9
color = ('blue', 'red', 'green')
for shape_of_side in range(3, no_of_sides+1):
    timmy.color(color[shape_of_side % len(color)])
    draw_shape(shape_of_side)


screen = Screen()
screen.exitonclick()
