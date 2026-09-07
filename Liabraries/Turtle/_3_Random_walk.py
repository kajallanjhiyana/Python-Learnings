from turtle import *
import random

directions = [0, 90, 180, 270]
tim = Turtle()
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))