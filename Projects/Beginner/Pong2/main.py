from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# These remember whether the ball was ALREADY touching a paddle on the
# previous frame -- so we only bounce the MOMENT contact starts,
# not on every single frame the ball happens to still be overlapping it.
was_touching_r_paddle = False
was_touching_l_paddle = False

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    touching_r_paddle = r_paddle.is_touching(ball)
    touching_l_paddle = l_paddle.is_touching(ball)

    if touching_r_paddle and not was_touching_r_paddle:
        ball.bounce = True
        ball.setangle()
        print("i am near right paddle")
        # ball.move()
    elif touching_l_paddle and not was_touching_l_paddle:
        ball.bounce = False
        ball.setangle()
        print("i am near left paddle")
        # ball.move()
    elif ball.xcor() > 400 or ball.xcor() < -400:
        ball.reset()

    was_touching_r_paddle = touching_r_paddle
    was_touching_l_paddle = touching_l_paddle

screen.exitonclick()