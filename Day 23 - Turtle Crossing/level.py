from turtle import Turtle
from constants import LEFT, TOP
import time

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.reset()
        self.update()
        
    def level_up(self):
        self.level += 1
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = ("Times New Roman", 20, "normal"))
        
    def game_over(self):
        self.clear()
        self.teleport(0, 0)
        self.write(f"Game Over!\nLevel: {self.level}", align = "center", font = ("Times New Romal", 40, "normal"))
        time.sleep(1)
        
    def reset(self):
        self.clear()
        self.teleport(LEFT + 20, TOP + 5)
        self.level = 1
        self.update()