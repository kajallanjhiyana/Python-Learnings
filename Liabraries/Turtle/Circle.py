import turtle

t = turtle.Turtle()

radius = 180
steps = 360                     # more steps = smoother circle
circumference = 2 * 3.14159 * radius
step_length = circumference / steps
turn_angle = 360 / steps

for _ in range(steps):
    t.forward(step_length)
    t.left(turn_angle)

turtle.done()