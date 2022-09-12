import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = range(360)
tim.pensize(1)
tim.speed("fastest")

while True:
    tim.color(random_color())
    tim.forward(2)
    tim.setheading(random.choice(directions))

