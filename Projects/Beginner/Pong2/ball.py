from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.angle = [30, 40, 50, 60, 70, 120, 130, 140, 150, 160]
        self.bounce = False
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        if self.ycor() > 280 and self.ycor() < 282: # It will bounce when y coordinate will be 281
            self.bounce = True 
            print("i am here")
        elif self.ycor() < -280 and self.ycor() > -282: #It will only execute when y coordinate will be -281
            self.bounce = False
        if self.bounce == True:
            self.setheading(random.choice(self.angle))
            # new_x = self.xcor() - 0.1
            # new_y = self.ycor() - 0.2
            # self.goto(new_x, new_y)
            self.forward(-0.1)
        
        elif self.bounce == False:
            self.setheading(random.choice(self.angle))
            # new_x = self.xcor() + 0.1
            # new_y = self.ycor() + 0.2
            # self.goto(new_x, new_y)
            self.forward(0.1)
        # print(self.bounce)
        
