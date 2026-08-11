from constants import BORDER_LENGTH, BORDER_WIDTH
from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.draw()
        
    
    def draw(self):
        self.teleport(-BORDER_LENGTH / 2, BORDER_WIDTH / 2)
        self.setposition(BORDER_LENGTH / 2, BORDER_WIDTH / 2)
        self.setposition(BORDER_LENGTH / 2, -BORDER_WIDTH / 2)
        self.setposition(-BORDER_LENGTH / 2, -BORDER_WIDTH / 2)
        self.setposition(-BORDER_LENGTH / 2, BORDER_WIDTH / 2)
        
        
