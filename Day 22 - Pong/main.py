from ball import Ball
from paddle import Paddle
from bot import Bot
from scoreboard import Scoreboard, Result
from border import Border
from constants import LEFT, RIGHT
# from turtle import Turtle
from screen_setup import screen
import time


restart = True


def restart():
    ...
    

def initialize():
    ...
    


def main():
    game_over = False
    
    screen.listen()
    
    border = Border()
    border.draw()
    
    player_1 = screen.textinput("Choose player names", "Player 1: ")
    player_2 = screen.textinput("Choose player names", "Player 2: ")
    
    ball = Ball()
    paddle_1 = Paddle(LEFT)
    
    paddle_1.name = player_1
    
    if player_2 == "":
        bot = Bot()
        paddle_2 = bot
        player_2 = "Bot"
        paddle_2.name = player_2
    else:
        paddle_2 = Paddle(RIGHT) 
    paddle_2.name = player_2
    
    scoreboard = Scoreboard()
    scoreboard.update()
    
    screen.onkeypress(paddle_1.move_up, "w")
    screen.onkeypress(paddle_1.move_down, "s")
    
    screen.onkeypress(paddle_2.move_up, "Up")
    screen.onkeypress(paddle_2.move_down, "Down")
    
    
    while not game_over:
        screen.listen()
        scoreboard.update()
        if player_2 == "Bot":
            bot.move(ball)
        loser, game_over = ball.move(paddle_1, paddle_2)
        screen.update()
        time.sleep(0.01)
        
    if loser == paddle_1.name: 
        winner = paddle_2.name
    else: 
        winner = paddle_1.name
    
    result = Result(loser, winner)
    result.update()
    screen.update()
    time.sleep(2)
            
    screen.bye()


if __name__ == "__main__":
    main()