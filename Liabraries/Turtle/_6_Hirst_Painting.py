import colorgram
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()
tim.speed(0)
tim.penup()
tim.hideturtle()

#Extracts colours from the image 
colors = colorgram.extract('/home/kajal/Documents/Python-Revision/Liabraries/Turtle/image.png', 38)
# print(colors)
l = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    l.append((r, g, b)) #Adds colours to the list from the image

#Sets positions to where to start from
tim.setheading(210)
tim.forward(1600)
tim.setheading(0)
number_of_dots = 9*15

for i in range(1, number_of_dots+1):
    tim.dot(100, random.choice(l))
    tim.forward(200)
    if i % 15 == 0:
        tim.setheading(90)
        tim.forward(200)
        tim.setheading(180)
        tim.forward(30*100)
    tim.setheading(0)

screen.exitonclick()


