from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)   # 100px tall, 20px wide
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 280:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -280:
            self.goto(self.xcor(), new_y)

    def is_touching(self, ball):
        # Box check: 20px half-width, 60px half-height (with a little cushion).
        within_x = abs(ball.xcor() - self.xcor()) < 20
        within_y = abs(ball.ycor() - self.ycor()) < 60
        return within_x and within_y