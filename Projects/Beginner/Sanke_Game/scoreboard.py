from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.high_score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def writeinfile(self, content):
        with open("/home/kajal/Documents/Python-Revision/Projects/Beginner/Sanke_Game/data.txt", mode = "w") as file:
            file.write(content)
             
    def reset(self):
        if self.score > self.high_score:
            self.score = 0
            with open("/home/kajal/Documents/Python-Revision/Projects/Beginner/Sanke_Game/data.txt", mode = "r") as file:
                content = file.read()
                if content == "":
                    self.writeinfile(content)
                elif int(content) < self.score:
                    self.highscore = self.score
                    self.writeinfile(content)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()
