import turtle
import random

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

for n in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)

    shape = random.randint(3, 12)
    direction = 360 / shape + 2

    pensize = random.randint(1, 5)
    t.pensize(pensize)

    angle = t.heading()     # remember the angle

    x = random.randrange(0, turtle.window_width() // 2)
    y = random.randrange(0, turtle.window_height() // 2)

    # 1st spiral
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(angle) # set the angle
    for m in range(size):
        t.forward(m*2)
        t.left(direction)

    # 2nd spiral
    t.penup()
    t.goto(-x, y)
    t.pendown()
    t.setheading(180 - angle) # set the angle
    for m in range(size):
        t.forward(m*2)
        t.left(direction)

    # 3rd spiral
    t.penup()
    t.goto(-x, -y)
    t.pendown()
    t.setheading(180 + angle) # set the angle
    for m in range(size):
        t.forward(m*2)
        t.left(direction)

    # 4th spiral
    t.penup()
    t.goto(x, -y)
    t.pendown()
    t.setheading(360 - angle) # set the angle
    for m in range(size):
        t.forward(m*2)
        t.left(direction)
