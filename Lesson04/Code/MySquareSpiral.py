# My first Square Spiral

import turtle

turtle.bgcolor('black')
turtle.title("Square Spiral")

t = turtle.Pen()
t.speed(0)

colors = ['magenta', 'blue', 'green', 'purple', 'orange', 'gold', 'yellow']
n = len(colors)

for x in range(200):
    t.pencolor(colors[x % n])
    t.width(x/20 + 1)
    t.forward(x * 3)
    t.left(91)
