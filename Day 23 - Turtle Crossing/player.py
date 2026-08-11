from turtle import Turtle
import constants

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.teleport(0, constants.BOTTOM - 20)

    def move_up(self):
        if self.ycor() <= constants.TOP:
            self.sety(self.ycor() + 10)
    
    def move_down(self):
        if self.ycor() > constants.BOTTOM - 20:
            self.sety(self.ycor() - 10)
