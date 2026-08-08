from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# Higher order functions are functions that take other function as parameter and/or returns a function
def turn_left():
    timmy.setheading(timmy.heading() + 10)
    
def turn_right():
    timmy.setheading(timmy.heading() - 10)
    
def forward():
    timmy.forward(10)

def backward():
    timmy.backward(10)
    
def clear():
    timmy.reset()


screen.listen()
screen.onkey(clear, "c")
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.exitonclick()