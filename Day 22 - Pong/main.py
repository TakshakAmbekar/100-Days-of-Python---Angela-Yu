from ball import Ball
from paddle import Paddle
from bot import Bot
from scoreboard import Scoreboard, Result
from border import Border
from constants import LEFT, RIGHT
from screen_setup import screen
import time


def restart():
    ball.reset()
    scoreboard.reset()
    result.reset()
    paddle_1.reset()
    paddle_2.reset()
    bot.reset()
    main()

def initialize():
    screen.listen()
    scoreboard.update(0)
    screen.update()
    
    player_1_name = screen.textinput("Choose player names", "Player 1: ")
    player_1 = paddle_1
    player_1.name = player_1_name
    
    player_2_name = screen.textinput("Choose player names", "Player 2: (Press enter to play against bot)")
    if player_2_name == "":
        player_2 = bot
        bot.showturtle()
        paddle_2.hideturtle()
    else:
        player_2 = paddle_2
        bot.hideturtle()
        paddle_2.showturtle()
    player_2.name = player_2_name
    
    scoreboard.update(0)
    
    screen.onkeypress(paddle_1.up_press, "w")
    screen.onkeyrelease(paddle_1.up_release, "w")

    screen.onkeypress(paddle_1.down_press, "s")
    screen.onkeyrelease(paddle_1.down_release, "s")
    
    if player_2 != bot:
        screen.onkeypress(player_2.up_press, "Up")
        screen.onkeyrelease(player_2.up_release, "Up")

        screen.onkeypress(player_2.down_press, "Down")
        screen.onkeyrelease(player_2.down_release, "Down")
    
    return player_1, player_2

def play(player_1, player_2, game_over):
    while not game_over:
        screen.listen()
        player_1.move()
        scoreboard.update(ball.bounce_count)
        if player_2 == bot:
            player_2.move(ball)
        else:
            player_2.move()
        loser, game_over = ball.move(player_1, player_2)
        screen.update()
        time.sleep(0.01)
    return loser, game_over


border = Border()
border.draw()
ball = Ball()
scoreboard = Scoreboard()

paddle_1 = Paddle(LEFT)
paddle_2 = Paddle(RIGHT)
bot = Bot()
result = Result()

def main():
    game_over = False
    
    player_1, player_2 = initialize()
        
    loser, game_over = play(player_1, player_2, game_over)

        
    if loser == player_1.name: 
        winner = player_2.name
    else: 
        winner = player_1.name
        
    result.loser = loser 
    result.winner = winner
    
    
    result.update()
    screen.update()
    
    time.sleep(1)
            
    wants_restart = screen.textinput("Play another match?", "Press 'y' to play another match, 'q' to quit") == "y"
    if wants_restart:
        restart()
    else:
        screen.bye()
        

if __name__ == "__main__":
    main()