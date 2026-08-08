from turtle import Turtle, Screen

timmy = Turtle()
timmy.color("black", "orange")
timmy.speed(2)

def starting_pos():
    timmy.penup()
    timmy.goto(-300,0)
    timmy.pendown()

def stroke():
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

starting_pos()
for _ in range(50):
    stroke()


screen = Screen()
screen.exitonclick()