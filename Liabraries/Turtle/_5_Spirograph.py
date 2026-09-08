from turtle import *

screen = Screen()
tim = Turtle()
gap = 10
screen.bgcolor("black")
tim.speed(0)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

for i in range(36):
    tim.pencolor(colors[i % len(colors)])
    tim.circle(150)
    tim.left(gap)

tim.done()