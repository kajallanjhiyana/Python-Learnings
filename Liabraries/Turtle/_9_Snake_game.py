from turtle import Turtle, Screen
import random

tim = Turtle()
snake_obj = Turtle("circle")
snake_obj.color("gray")
snake_body = []
food_obj = Turtle()
screen = Screen()
is_game_on = True
food_ate = False
tail_length = 3
last_speed_up_score = 0

screen.setup(width = 1200, height = 1200)
screen.bgcolor("black")
screen.title("Snake game")

#! Move Snake
#Move right
def move_right():
    snake_obj.setheading(0)


#Move left
def move_left():
    snake_obj.setheading(180)

#Move up
def move_up():
    snake_obj.setheading(90)

#Move Down
def move_down():
    snake_obj.setheading(270)

#! Manage Score
# Write Score on Top
score = -1
tim.hideturtle()
def update_score():
    global score
    score += 1
    tim.penup()
    tim.goto(0, 500)
    tim.color("white")
    tim.clear()
    tim.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

#! Manage Food
#Generate food
def generate_food():
    food_colors = ["red", "orange", "yellow", "green", "cyan", "magenta", "purple", "pink", "gold", "lime"]
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    food_obj.clear()
    food_obj.penup()
    food_obj.hideturtle()
    food_obj.goto(x, y)
    food_obj.color(random.choice(food_colors))
    food_obj.dot(30)
    
    

#!Increase speed of snake
def increase_speed():
    global current_speed
    if current_speed < 10:
        current_speed += 2
        snake_obj.speed(current_speed)
        for segment in snake_body:
            segment.speed(current_speed)
    print("speed =", current_speed)

#! Track if food is ate
def food_ate_check():
    global food_ate
    if snake_obj.distance(food_obj)<15 or (snake_obj.xcor() == food_obj.xcor() and snake_obj.ycor() == food_obj.ycor()):
        food_ate = True

#Increase snake's size
def increase_snake_size():
    global tail_length
    tail_length += 1
    snake_obj2 = Turtle("square")
    snake_obj2.color("white")
    snake_obj2.speed(current_speed)   # match current game speed, not default 3
    snake_obj2.penup()
    screen.tracer(0)

    if len(snake_body) > 0:
        last_x, last_y = snake_body[-1].xcor(), snake_body[-1].ycor()
    else:
        last_x, last_y = snake_obj.xcor(), snake_obj.ycor()
    snake_obj2.goto(last_x, last_y)

    snake_body.append(snake_obj2)

# Move snake body 
def move_snake():
    # Move body segments, starting from the LAST one, moving toward the front
    for index in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[index - 1].xcor()
        new_y = snake_body[index - 1].ycor()
        snake_body[index].goto(new_x, new_y)

    # Move the first body segment to where the head currently is
    if len(snake_body) > 0:
        snake_body[0].goto(snake_obj.xcor(), snake_obj.ycor())

    # Finally move the head forward
    snake_obj.forward(10)

#! Fallback
def check_wall_collision():
    global is_game_on
    if snake_obj.xcor() > 590 or snake_obj.xcor() < -590 or \
       snake_obj.ycor() > 590 or snake_obj.ycor() < -590:
        is_game_on = False
        print("Wall collision occurred")

def check_tail_collision():
    global is_game_on
    for segment in snake_body[4:]:      # skip the 4 segments nearest the head
        if snake_obj.distance(segment) < 10:
            is_game_on = False
            print("Tail collision occurred")

def game_over():
    tim.penup()
    tim.goto(0, 0)
    tim.color("white")
    tim.write(f"GAME OVER\nScore: {score}", align="center", font=("Arial", 24, "normal"))

#Snake moving right always
snake_obj.home()
snake_obj.color("white")
snake_obj.setheading(0)
current_speed = 1
snake_obj.speed(current_speed) 
generate_food()
update_score()
while is_game_on:
    screen.listen()
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    snake_obj.penup()
    move_snake()
    food_ate_check()
    if food_ate:
        generate_food()
        food_ate = False
        update_score()
        increase_snake_size()
        screen.update()

    if score != 0 and score % 2 == 0 and score != last_speed_up_score:
        print("Speed is increased")
        increase_speed()
        increase_snake_size()
        last_speed_up_score = score

    check_wall_collision()
    check_tail_collision()

game_over()
screen.exitonclick()
