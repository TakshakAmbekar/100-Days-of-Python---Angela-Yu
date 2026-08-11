from constants import PADDLE_SPEED, PADDLE_LENGTH, LEFT, RIGHT, PADDLE_THICKNESS, TURTLE_SIZE, BORDER_WIDTH
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, name = "Player"):
        super().__init__()
        self.name = name
        self.x_pos = x_pos
        self.penup()
        self.teleport(x_pos, 0)
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(PADDLE_THICKNESS, PADDLE_LENGTH)
    
    def reset(self):
        self.teleport(self.x_pos, 0)
    
    def move_up(self):
        x, y = self.position()
        if y < BORDER_WIDTH / 2 - PADDLE_LENGTH * TURTLE_SIZE / 2:
            self.setheading(90)
            self.forward(TURTLE_SIZE)
    
    def move_down(self):
        x, y = self.position()
        if y > -BORDER_WIDTH / 2 + PADDLE_LENGTH * TURTLE_SIZE / 2:
            self.setheading(270)
            self.forward(TURTLE_SIZE)
        
            
    