from turtle import Turtle
from constants import LEFT, RIGHT, TOP, BOTTOM, COLORS
from random import randrange, choice


class Car(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 3)
        self.teleport(x, y)
        
    def move(self):
        self.setx(self.xcor() + 5)
        if self.xcor() > RIGHT + 15:
            self.reset_car()
    
    def reset_car(self):
        x = randrange(LEFT - 120, LEFT - 30, 10)
        y = randrange(BOTTOM + 50, TOP - 1, 60)
        # while True:
        #     valid_position_found = True
        #     for car in cars_set:
        #         if car.distance(x, y) <= 100:
        #             x = randrange(LEFT - 120, LEFT - 30, 10)
        #             y = randrange(BOTTOM + 50, TOP - 1, 60)
        #             valid_position_found = False
        #             break
            
        #     if valid_position_found == True:
        #         break
                    
        self.teleport(x, y)
        
class Cars():
    def __init__(self):
        self.car_set = set()
        for _ in range(20):
            x = randrange(LEFT, RIGHT, 10)
            y = randrange(BOTTOM + 50, TOP - 1, 60)
            # while True:
            #     valid_position_found = True
            #     for car in cars_set:
            #         if car.distance(x, y) <= 100:
            #             x = randrange(LEFT, RIGHT, 10)
            #             y = randrange(BOTTOM + 50, TOP - 1, 60)
            #             valid_position_found = False
            #             break
                
            #     if valid_position_found == True:
            #         break
    
            car = Car(x, y)
            car.color(choice(COLORS))
            self.car_set.add(car)        


    def reset(self):
        for car in self.car_set:
            x = randrange(LEFT, RIGHT, 10)
            y = randrange(BOTTOM + 50, TOP - 1, 60)
            # while True:
            #     valid_position_found = True
            #     for car in cars_set:
            #         if car.distance(x, y) <= 100:
            #             x = randrange(LEFT, RIGHT, 10)
            #             y = randrange(BOTTOM + 50, TOP - 1, 60)
            #             valid_position_found = False
            #             break
                
            #     if valid_position_found == True:
            #         break
    
            car.teleport(x,y)