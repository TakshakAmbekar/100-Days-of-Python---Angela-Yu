from turtle import Turtle, Screen 
from snake import Snake
from food import Food
import time

BORDER_LENGTH = 300


game_on = True
while game_on:
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
    food = Food()

    food.create_food(snake)

    screen.listen()
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_down, "s")
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_right, "d")
    

    while not snake.busted():
        
        snake.move()
        snake.distance(food.food_list, food.create_food)
        screen.update()
        time.sleep(0.1)
    
    game_on = screen.textinput("Game Over!", "Play again? (y/n)".strip().lower()) == 'y'   
    screen.clear()     


screen.bye()