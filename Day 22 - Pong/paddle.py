from constants import PADDLE_SPEED, PADDLE_LENGTH, LEFT, RIGHT, PADDLE_THICKNESS, TURTLE_SIZE, BORDER_WIDTH, PADDLE_SPEED
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, name = "Player"):
        super().__init__()
        self.name = name
        self.x_pos = x_pos
        self.up_pressed = False
        self.down_pressed = False
        self.penup()
        self.teleport(x_pos, 0)
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(PADDLE_THICKNESS, PADDLE_LENGTH)
    
    def reset(self):
        self.teleport(self.x_pos, 0)
        self.up_pressed = False
        self.down_pressed = False
    
    def move(self):
        if self.up_pressed and self.ycor() < BORDER_WIDTH / 2 - PADDLE_LENGTH * TURTLE_SIZE / 2:
            self.sety(self.ycor() + PADDLE_SPEED)
        if self.down_pressed and self.ycor() > -BORDER_WIDTH / 2 + PADDLE_LENGTH * TURTLE_SIZE / 2:
            self.sety(self.ycor() - PADDLE_SPEED)
    
    def up_press(self):
        self.up_pressed = True

    def up_release(self):
        self.up_pressed = False

    def down_press(self):
        self.down_pressed = True

    def down_release(self):
        self.down_pressed = False
        
            
    