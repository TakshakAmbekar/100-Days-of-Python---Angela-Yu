from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.color("black", "orange")
timmy.speed(0)
timmy.pensize(1)
colormode(255)


def choose_color():
    timmy.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    
def circle():
    choose_color()
    timmy.circle(100)
    

for _ in range(90):
    circle()
    timmy.left(4)


screen = Screen()
screen.exitonclick()