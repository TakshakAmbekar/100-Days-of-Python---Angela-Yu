from turtle import Turtle, Screen, colormode
import random
import colorgram

colors = colorgram.extract("Day 18 - GUI/hirst_dot_painting.jpg", 10)

timmy = Turtle()

timmy.speed(0)
timmy.pensize(10)
timmy.penup()
timmy.setposition(-200, 200)
colormode(255)


def choose_color():
    timmy.pencolor(random.choice(colors).rgb)
    
def horizontal():
    for _ in range(10):
        choose_color()
        timmy.dot()
        timmy.forward(40)

def vertical():
    horizontal()
    x,y = timmy.position()
    timmy.setposition(-200, y - 40)
    

for _ in range(10):
    vertical()


screen = Screen()
screen.exitonclick()