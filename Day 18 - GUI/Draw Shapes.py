from turtle import Turtle, Screen

timmy = Turtle()
timmy.color("black", "orange")
timmy.speed(0)

timmy.penup()
timmy.goto(0, -200)
timmy.pendown()

full_angle = 360

for side in range(3, 11):
    rotate = 360 / side
    for i in range(side):
        timmy.forward(100)
        timmy.left(rotate)


screen = Screen()
screen.exitonclick()