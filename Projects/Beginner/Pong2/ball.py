from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.bounce = False
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def setangle(self):
        a = random.randint(10, 70)
        if self.bounce == True:
            a = random.randint(10, 70)
        else:
            a = random.randint(70, 180)
        self.setheading(a)
        print(a)

    def reset(self):
        self.goto(0, 0)   # FIX: goto() needs BOTH x and y -- goto(0,) was missing the y and crashed

    def move(self):
        if self.ycor() > 280 and self.ycor() < 282: # It will bounce when y coordinate will be 281
            self.bounce = True 
            print("True I bounced at +ve angle")
            self.setangle()
        elif self.ycor() < -280 and self.ycor() > -282: #It will only execute when y coordinate will be -281
            self.bounce = False
            self.setangle()
            print("False I bounced at +ve angle")
        if self.bounce == True:
            # new_x = self.xcor() - 0.1
            # new_y = self.ycor() - 0.2
            # self.goto(new_x, new_y)
            self.forward(-0.1)
        
        elif self.bounce == False:
            # new_x = self.xcor() + 0.1
            # new_y = self.ycor() + 0.2
            # self.goto(new_x, new_y)
            self.forward(0.1)
        # print(self.bounce)