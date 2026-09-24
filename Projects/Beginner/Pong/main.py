import time
from turtle import Screen
from ball import Ball
from Paddle import Paddle
from scoreboard import Scoreboard

WINNING_SCORE = 5

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Paddle bounce (only near the correct side, cheap check first)
    if ball.xcor() > 350 and r_paddle.is_touching(ball):
        ball.bounce_paddle(r_paddle)
    elif ball.xcor() < -350 and l_paddle.is_touching(ball):
        ball.bounce_paddle(l_paddle)

    # Missed -- someone scores
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position(direction=-1)
    elif ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position(direction=1)

    # Win condition
    if scoreboard.l_score == WINNING_SCORE:
        scoreboard.game_over("Left player")
        game_is_on = False
    elif scoreboard.r_score == WINNING_SCORE:
        scoreboard.game_over("Right player")
        game_is_on = False

screen.exitonclick()