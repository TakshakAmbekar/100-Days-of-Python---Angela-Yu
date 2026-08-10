from turtle import Turtle
from constants import BORDER_LENGTH, BORDER_WIDTH, FONT

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.teleport(BORDER_LENGTH / 2, BORDER_WIDTH)
        
    def update(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align = "center", font = FONT)
        
    def reset(self):
        self.clear()

class Result(Scoreboard):
    def __init__(self, loser, winner):
        super().__init__()
        self.loser = loser
        self.winner = winner
        self.teleport(0, 0)
        
    def update(self):
        self.clear()
        self.write(f"{self.loser} lost the ball. \n{self.winner} wins!", align = "center", font = ("Times New Roman", 30, "normal"))
        