from turtle import Turtle, Screen 
from snake import Snake, ScoreBoard
from food import Food
import time

BORDER_LENGTH = 300



def restart_game():
    global restart
    restart = True
    screen.clear()
    
def quit_game():
    global game_on
    game_on = False
    screen.bye()
    
game_on = True

while game_on:
    restart = False
    screen = Screen()
    screen.setup(800, 800)
    screen.tracer(0)


    border = Turtle()
    border.teleport(-BORDER_LENGTH, -BORDER_LENGTH)
    for _ in range(4):
        border.forward(2 * BORDER_LENGTH)
        border.left(90)
    border.hideturtle()
    
    snake = Snake()
    food_spawn = Food()

    food_spawn.create_food(snake)

    screen.listen()
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_down, "s")
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_right, "d")
    

    while not snake.busted():
        snake.move(food_spawn, food_spawn.create_food)
        screen.update()
        time.sleep(0.1)
    
    snake.game_over(screen)
    
    screen.onkey(restart_game,"space") 
    screen.onkey(quit_game, "q")
    
    while not restart and game_on:
        screen.update()
        time.sleep(0.1)  