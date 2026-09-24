from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        # Velocity vector: how far to move each frame, on each axis.
        # No angles, no trig -- just two numbers that get added to position.
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1   # controls frame delay in the main loop

    def move(self):
        # ONE goto() call per frame, instead of hundreds of tiny forward() calls.
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        # Top/bottom wall: just flip vertical direction. Horizontal is untouched,
        # so the ball keeps its left-right motion instead of losing it.
        self.y_move *= -1

    def bounce_paddle(self, paddle):
        # "Diving board" bounce: how far from the paddle's center did it hit?
        offset = self.ycor() - paddle.ycor()
        self.x_move *= -1
        self.y_move = offset * 0.3   # steeper near the edges, flatter near the middle

        # Speed up slightly after every paddle hit -- makes rallies escalate,
        # which is what real arcade Pong does.
        if abs(self.x_move) < 40:   # cap it so it doesn't become unplayable
            self.x_move *= 1.05

    def reset_position(self, direction=1):
        self.goto(0, 0)
        self.x_move = 10 * direction   # relaunch toward whoever just got scored on
        self.y_move = 10