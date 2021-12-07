import turtle
import random
import math
from turtle import Turtle, Screen
directions = [0, 90, 180, 270]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)


tim = Turtle()
tim.shape('turtle')
tim.speed(20)
tim.color('cyan4')
tim.shapesize(2, 2, 2)
tim.pensize(1)
moves = 0
# while moves < 101:
#     moves += 1
#     if -100 < tim.xcor() < 300 and -100 < tim.ycor() < 300:
#         tim.right(random.randint(0, 360))
#         tim.forward(random.randint(0, 200))
#         tim.pencolor(random.choice(colours))
#
#     else:
#         tim.right(180)
#         tim.forward(random.randint(0, 300))
#         tim.color(random.choice(colours))

# for _ in range(200):
#     random_color()
#     tim.forward(random.randint(50, 60))
#     tim.setheading(random.choice(directions))
for _ in range(int(360/1)):
    random_color()
    tim.setheading(tim.heading() + 1)
    tim.circle(60)


import heroes
print(heroes.gen())


screen = Screen()
screen.screensize(1000, 1000)
screen.exitonclick()

