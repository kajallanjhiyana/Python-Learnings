from turtle import *
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270] #It will walk only n, e, w, s
tim = Turtle()
tim.pensize(15)
tim.speed("fastest")
colormode(255)
color = ["red", "blue", "green", "pink", "yellow", "black", "orange", "purple"]
for _ in range(200):
    tim.forward(30)
    directions = random.randint(0, 360) #It can walk in any direction at any angle
    tim.setheading(directions)
    tim.pencolor(random_color())
