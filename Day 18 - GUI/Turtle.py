from turtle import Turtle, Screen as T , S

timmy = T()
timmy.color("black", "orange")
timmy.speed(2)

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


screen = S()
screen.exitonclick()