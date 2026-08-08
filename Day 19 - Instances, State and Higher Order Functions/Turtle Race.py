from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(800, 600)

referee = Turtle()
referee.hideturtle()
referee.speed(0)
referee.teleport(-290, 200)
referee.setposition(-290, -200)
referee.teleport(300, 200)
referee.setposition(300, -200)

def draw_lines(ref):
    for i in range(8):
        ref.teleport(-320, (3 - i) * 50 + 25)
        ref.setposition(320, (3 - i) * 50 + 25)
    
draw_lines(referee)


turtles = []
colors = ["red", "green", "purple", "pink", "blue", "black", "brown"]


def move(turtle):
    turtle.forward(random.randint(1, 20))


for i in range(7):
    offset = 3 - i
    t = Turtle()
    t.color(colors[i])
    t.penup()
    t.shape("turtle")
    t.teleport(-300, offset * 50)
    turtles.append(t)
    
is_race_on = False
winner = ""
guess = ""
while not guess:
    guess = screen.textinput("Make a guess", "Enter the color of turtle that will win")
if guess:
    is_race_on = True
    
while is_race_on:
    game_on = True
    for turtle in turtles:
        move(turtle)
        x, y = turtle.position()
        if x >= 290:
            winner = turtle.color()[0]
            game_on = False
    
    if not game_on:
        break
       
if winner == guess:
    print(f"Your guess was right! {winner} won!")
else:
    print(f"{guess} didn't win... Winner was {winner}")
screen.exitonclick()