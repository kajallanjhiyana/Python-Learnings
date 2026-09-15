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
speed = 10
def set_speed():
    global snake_obj
    s = snake_obj.speed()
    print(s)
    if s <10:
        snake_obj.speed(s+1)

#! Track if food is ate
def food_ate_check():
    global food_ate
    # print("for snake")
    # print("x = ", snake_obj.xcor())
    # print("y = ", snake_obj.ycor())
    # print("for food")
    # print("x = ", food_obj.xcor())
    # print("y = ", food_obj.ycor())
    if snake_obj.distance(food_obj)<15 or (snake_obj.xcor() == food_obj.xcor() and snake_obj.ycor() == food_obj.ycor()):
        food_ate = True
        print("Food ate")

#Increase snake's size
def increase_snake_size():
    global tail_length
    tail_length +=1
    snake_obj2 = Turtle("square")
    snake_obj2.color("white")
    snake_obj2.speed(1)
    snake_body.append(snake_obj2)
    snake_obj2.penup()  

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

def check_tail_collision():
    global is_game_on
    for segment in snake_body:
        if snake_obj.distance(segment) < 10:
            is_game_on = False

def game_over():
    tim.penup()
    tim.goto(0, 0)
    tim.color("white")
    tim.write(f"GAME OVER\nScore: {score}", align="center", font=("Arial", 24, "normal"))

#Snake moving right always
snake_obj.home()
snake_obj.color("white")
snake_obj.setheading(0)
snake_obj.speed(1)
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

    if score!= 0 and score%5 == 0:
        print("Speed is increased")
        set_speed()
    check_wall_collision()
    check_tail_collision()

game_over()
screen.exitonclick()
