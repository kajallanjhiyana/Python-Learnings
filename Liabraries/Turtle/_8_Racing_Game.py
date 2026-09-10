from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 1000, height = 1000)
is_raceon = False
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color:")
y_positions = [-300, -200, -100, 0, 100, 200]
colours = ["red", "yellow", "green", "blue", "pink", "purple"]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.goto(x = -470, y = y_positions[i])
    new_turtle.color(colours[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_raceon = True

while is_raceon:
    for turtle in all_turtles:
        if turtle.xcor() > 470:
            is_raceon = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner")
            else:
                print(f"You've lost! The {winning_color} turtle is winner")
        rand_distances = random.randint(0, 10)
        turtle.forward(rand_distances)

screen.exitonclick()