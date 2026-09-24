from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 280:                  # FIX: stop the paddle from flying off the top edge
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -280:                 # FIX: stop the paddle from flying off the bottom edge
            self.goto(self.xcor(), new_y)

    def is_touching(self, ball):
        # Draw an invisible box around the paddle.
        # left_edge / right_edge = the box's boundaries side-to-side.
        # 20 pixels of "cushion" on each side, past the paddle's actual center.
        left_edge = self.xcor() - 20
        right_edge = self.xcor() + 20
 
        # top_edge / bottom_edge = the box's boundaries up-and-down.
        # 60 pixels of cushion because this paddle is tall (stretched 5x taller
        # than a normal turtle square, so it reaches roughly 50px above and
        # below its center -- 60 gives it a little extra room).
        top_edge = self.ycor() + 60
        bottom_edge = self.ycor() - 60
 
        # Question 1: is the ball's LEFT-RIGHT position inside the box?
        # (True only if the ball's x is strictly between left_edge and right_edge)
        ball_is_between_left_and_right = left_edge < ball.xcor() < right_edge
 
        # Question 2: is the ball's UP-DOWN position inside the box?
        # (True only if the ball's y is strictly between bottom_edge and top_edge)
        ball_is_between_top_and_bottom = bottom_edge < ball.ycor() < top_edge
 
        # The ball only counts as "touching" the paddle if BOTH questions are
        # true at the same time -- lined up correctly left-right AND at a
        # height where the paddle actually exists.
        return ball_is_between_left_and_right and ball_is_between_top_and_bottom