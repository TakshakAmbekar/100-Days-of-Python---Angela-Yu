from turtle import Turtle
from constants import TOP, BOTTOM

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.reset()
        self.up_pressed = False
        self.down_pressed = False
        
    def up_press(self):
        self.up_pressed = True
    def up_release(self):
        self.up_pressed = False
    
    def down_press(self):
        self.down_pressed = True
    def down_release(self):
        self.down_pressed = False
        

    def move(self, level_up):
        if self.up_pressed and self.ycor() < TOP + 30:
            self.sety(self.ycor() + 5)
        
        if self.down_pressed and self.ycor() > BOTTOM - 20:
            self.sety(self.ycor() - 5)
            
        if self.ycor() >= TOP + 30:
            level_up()
            self.reset()
            return True
        
    def crash(self, car_pos):
        player_x, player_y = self.position()
        car_x, car_y = car_pos
        if abs(car_x - player_x) <= 30 and abs(car_y - player_y) <= 10:
            return True
        return False
            
    def reset(self):
        self.teleport(0, BOTTOM - 20)
        self.up_pressed = False
        self.down_pressed = False
