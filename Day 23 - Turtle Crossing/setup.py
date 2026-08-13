from turtle import Screen
from constants import TOP, BOTTOM, LEFT, RIGHT, WIDTH, HEIGHT, COLORS
from random import randrange, choice
from car import Cars
from road import Road
from player import Player
from level import Level


road = Road()
player = Player()
level = Level()
cars = Cars()

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.up_press, "w")
screen.onkeyrelease(player.up_release, "w")
screen.onkeypress(player.down_press, "s")
screen.onkeyrelease(player.down_release, "s")


def reset():
    road.draw()
    player.reset()
    level.reset()
    cars.reset()
    screen.update()
    screen.listen()
    


