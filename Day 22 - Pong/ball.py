from turtle import Turtle
from constants import BALL_SPEED, BALL_SIZE, BORDER_WIDTH, BORDER_LENGTH, TURTLE_SIZE, PADDLE_LENGTH, PADDLE_THICKNESS
from random import randint, choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(BALL_SIZE)
        self.color("white")
        self.speed = BALL_SPEED
        self.vector = [choice([-1, 1]) * BALL_SPEED * randint(2, 5), choice([-1, 1]) * BALL_SPEED * randint(2, 5)]   
        
    def move(self, paddle_1, paddle_2):
        x, y = self.position()
        delta_x, delta_y = self.vector
        self.teleport(x + delta_x, y + delta_y)
        self.collision_with_wall()
        self.collision_with_pad(paddle_1)
        self.collision_with_pad(paddle_2)
        if self.ball_went_past(paddle_1):
            # return losing player name and True for game_over boolean
            return paddle_1.name, True
        if self.ball_went_past(paddle_2):
            return paddle_2.name, True
        return "", False
        
    def collision_with_wall(self):
        x, y = self.position()
        
        if (self.distance(x, BORDER_WIDTH / 2) <= TURTLE_SIZE * BALL_SIZE / 2 or 
            self.distance(x, -BORDER_WIDTH / 2) <= TURTLE_SIZE * BALL_SIZE / 2):
            self.vector[1] *= -1
            
    def ball_went_past(self, paddle):
        ball_x, ball_y = self.position()
        pad_x, pad_y = paddle.position()
        if ((pad_x < 0 and ball_x < pad_x) or
            (pad_x > 0 and ball_x > pad_x)):
            return True
    
    def collision_with_pad(self, paddle):
        x, y = self.position()
        pad_x, pad_y = paddle.position()
        if (self.distance(pad_x, y) <= TURTLE_SIZE * BALL_SIZE / 2 and 
            pad_y - PADDLE_LENGTH * TURTLE_SIZE / 2 <= y <= pad_y + PADDLE_LENGTH * TURTLE_SIZE / 2):
            self.vector[0] *= -1
            return True