from random import randrange
from turtle import Turtle, Screen

class Food():
    def __init__(self):
        food = Turtle()
        self.food = food
        food.penup()
        food.shape("circle")
        food.color("black")
        
        
    def create_food(self, snake):
        food = self.food
        segments = []
        for segment in snake.snake:
            segments.append(segment.position())
        
        (x, y) = (randrange(-270, 270, 20), randrange(-270, 270, 20))
        
        while (x, y) in segments:
            (x, y) = (randrange(-270, 270, 20), randrange(-270, 270, 20))
        
        food.setposition(x, y)
        
    

        
    