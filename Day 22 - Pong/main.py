from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard, Result
from border import Border
from constants import LEFT, RIGHT
# from turtle import Turtle
from screen_setup import screen
import time


# t = Turtle()
# t.hideturtle()
# t.teleport(-300, 0)
# t.speed(0)
# t.color("white")
# t.setposition(300, 0)

def main():
    game_over = False
    
    border = Border()
    border.draw()
    
    player_1 = screen.textinput("Choose player names", "Player 1: ")
    player_2 = screen.textinput("Choose player names", "Player 2: ")
    loser = ""
    
    screen.listen()
    
    ball = Ball()
    paddle1 = Paddle(player_1, LEFT)
    paddle2 = Paddle(player_2, RIGHT)
    scoreboard = Scoreboard()
    scoreboard.update()
    
    screen.onkeypress(paddle1.move_up, "w")
    screen.onkeypress(paddle1.move_down, "s")
    
    screen.onkeypress(paddle2.move_up, "Up")
    screen.onkeypress(paddle2.move_down, "Down")
    
    
    while not game_over:
        scoreboard.update()
        loser, game_over = ball.move(paddle1, paddle2)
        screen.update()
        time.sleep(0.01)
        
    if loser == player_1: winner = player_2
    else: winner = player_1
    
    result = Result(loser, winner)
    result.update()
    screen.update()
    time.sleep(2)
            
    screen.bye()


if __name__ == "__main__":
    main()