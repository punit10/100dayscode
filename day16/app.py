from turtle import Turtle, Screen
from random import random
if __name__ == '__main__':
    print("Hi Python!")

tim = Turtle()
tim.shape("turtle")
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
for steps in range(10):
    for c in ('blue', 'red', 'green'):
        tim.color(c)
        tim.forward(steps)
        tim.right(30)
tim.forward(100)


t = Turtle()
t.shape("turtle")
for i in range(10):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)


window = Screen()
print(window.canvwidth, window.canvheight)
window.exitonclick()

from prettytable import PrettyTable

data_table = PrettyTable()
data_table.field_names = ["City", "Area", "Population", "Annual Rainfall"]
data_table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
print(data_table)

