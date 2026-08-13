from turtle import Turtle
from constants import TOP, BOTTOM, LEFT, RIGHT

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        
    def draw(self):
        self.teleport(LEFT, BOTTOM)
        self.setposition(RIGHT, BOTTOM)
        self.setposition(RIGHT, TOP)
        self.setposition(LEFT, TOP)
        self.setposition(LEFT, BOTTOM)
        return True

