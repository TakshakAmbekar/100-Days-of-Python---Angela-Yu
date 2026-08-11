from turtle import Turtle, Screen
from constants import TOP, BOTTOM, LEFT, RIGHT, WIDTH, HEIGHT

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

screen.listen()

road = Turtle()
road.hideturtle()
road.teleport(LEFT, BOTTOM)
road.setposition(RIGHT, BOTTOM)
road.setposition(RIGHT, TOP)
road.setposition(LEFT, TOP)
road.setposition(LEFT, BOTTOM)

