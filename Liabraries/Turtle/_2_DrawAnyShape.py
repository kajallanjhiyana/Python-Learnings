from turtle import *

screen = Screen()
tim = Turtle()

def draw(sides):
    angle = 360/sides
    for _ in range(0, sides):
        tim.forward(100)
        tim.left(angle)

sides = int(input("Enter no. of sides: "))
draw(sides)