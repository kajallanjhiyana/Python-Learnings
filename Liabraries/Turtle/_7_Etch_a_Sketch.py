from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.setheading(270)
    tim.forward()

def move_clockwise():
    #Turn right
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_anticlockwise():
    #Turn Left
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_clockwise, "a")
screen.onkey(move_anticlockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()