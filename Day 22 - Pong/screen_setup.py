from turtle import Screen 
from constants import BORDER_LENGTH, BORDER_WIDTH

screen = Screen()
screen.setup(BORDER_LENGTH + 200, BORDER_WIDTH + 100)
screen.tracer(0)
screen.listen()
screen.bgcolor("black")