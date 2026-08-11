from turtle import Turtle
from constants import LEFT, RIGHT, TOP, BOTTOM
from random import randrange, choice

cars_set = set()
colors = ["green", "red", "blue", "pink", "yellow", "purple", "orange", "brown"]

class Car(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 3)
        self.teleport(x, y)
        
    def move(self):
        self.setx(self.xcor() + 10)
        if self.xcor() > RIGHT + 30:
            self.reset_car()
    
    def reset_car(self):
        x = randrange(LEFT - 120, LEFT - 30, 10)
        y = randrange(BOTTOM + 50, TOP - 1, 60)
        while True:
            valid_position_found = True
            for car in cars_set:
                if car.distance(x, y) <= 150 and car.ycor() == y:
                    y = randrange(BOTTOM + 50, TOP - 1, 60)
                    valid_position_found = False
            
            if valid_position_found == True:
                break
                    
        self.teleport(x, y)
        
            
# Make the cars spawn on x coordinates as multiples of 10 and y coordinates depending on the number of lanes on the road
for i in range(20):
    x = randrange(LEFT, RIGHT, 10)
    y = randrange(BOTTOM + 50, TOP - 1, 60)
    while True:
        valid_position_found = True
        for car in cars_set:
            if car.distance(x, y) <= 150 and car.ycor() == y:
                y = randrange(BOTTOM + 50, TOP - 1, 60)
                valid_position_found = False
                break
        
        if valid_position_found == True:
            break

    car = Car(x, y)
    car.color(choice(colors))
    cars_set.add(car)
