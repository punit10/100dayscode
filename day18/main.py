from turtle import Turtle, Screen
import random


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
timmy.pensize(10)
turn = ('Right', 'Left')
def draw_shape(side):
    angle = 360/side
    for _ in range(side):
        timmy.forward(60)
        timmy.right(angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

no_of_sides = 2
color = ('blue', 'red', 'green', 'pink')
for shape_of_side in range(3, no_of_sides+1):
    timmy.color(color[shape_of_side % len(color)])
    draw_shape(shape_of_side)

timmy = Turtle()
timmy.pensize(10)
turn = (0, 1)
direction = (0, 90, 180)
for _ in range(20):
    timmy.color(random.choice(color))
    # timmy.right(90) if random.choice(turn) == 0 else timmy.left(90)
    timmy.forward(40)
    timmy.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
