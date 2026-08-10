from random import randrange
from turtle import Turtle, Screen

class Food():
    def __init__(self):
        self.food_list = []
        
    def create_food(self, snake):
        self.food_list = []
        segments = []
        for segment in snake.snake:
            segments.append(segment.position())
            
        (x, y) = (randrange(-270, 270, 20), randrange(-270, 270, 20))
        
        while (x, y) in segments:
            (x, y) = (randrange(-270, 270, 20), randrange(-270, 270, 20))
        
        new_food = Turtle()
        new_food.shape("circle")
        new_food.shapesize(0.6)
        new_food.teleport(x, y)
        
        self.food_list.append(new_food)

        
    