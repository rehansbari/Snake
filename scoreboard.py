from turtle import Turtle

STYLE = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0, 250)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=STYLE, align="center")

    def display_gameover(self):
            self.setpos(0,0)
            self.write("Game Over", font=STYLE, align="center")
