# from screen_setup import screen 
from screen_setup import screen, road
from player import Player
from cars import Car, cars_set
import time


player = Player()

screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")

screen.listen()

game_over = False

while not game_over:
    ...
    time.sleep(0.1)
    screen.update()
    for car in cars_set:
        car.move()