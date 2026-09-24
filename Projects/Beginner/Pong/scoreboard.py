from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_display()

    def update_display(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_display()

    def r_point(self):
        self.r_score += 1
        self.update_display()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"GAME OVER\n{winner} wins!", align="center", font=("Courier", 28, "normal"))