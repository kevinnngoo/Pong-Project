from turtle import Turtle
from ball import Ball
import time

ALIGNMENT = "CENTER"
FONT = ("COURIER",80,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()


    # def update_scoreboard(self):
    #     self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #
    # def increase_scoreboard(self):
    #     self.score +=1
    #     self.clear()
    #     self.update_scoreboard()