from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.color("black", "orange")
timmy.speed(0)
timmy.pensize(10)
colormode(255)


def choose_color():
    timmy.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    
def move():
    choose_color()
    timmy.forward(20)
    timmy.setheading(random.choice(headings))
    

headings = [0, 45, 90, 135, 180, 225, 270, 315]

for _ in range(500):
    move()


screen = Screen()
screen.exitonclick()