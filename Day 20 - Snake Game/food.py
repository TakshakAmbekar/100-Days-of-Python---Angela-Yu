from random import randrange
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("black")
        
        
    def create_food(self, snake):
        segments = []
        for segment in snake.snake:
            segments.append(segment.position())
        
        (x, y) = (randrange(-270, 270, 20), randrange(-270, 270, 20))
        
        while (x, y) in segments:
            (x, y) = (randrange(-270, 270, 20), randrange(-270, 270, 20))
        
        self.setposition(x, y)
        
    

        
    