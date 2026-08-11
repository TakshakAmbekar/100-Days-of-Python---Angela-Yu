from paddle import Paddle
from constants import RIGHT, BORDER_WIDTH, PADDLE_LENGTH, TURTLE_SIZE

class Bot(Paddle):
    def __init__(self, name = "Bot", x_pos = RIGHT):
        super().__init__(name, x_pos)
        self.teleport(RIGHT, 0)
        
    def move(self, ball):
        _, ball_y = ball.position()
        if ball_y >= 0:
            pad_y = min(ball_y, (BORDER_WIDTH / 2 -  PADDLE_LENGTH * TURTLE_SIZE / 2))
        else:
            pad_y = max(ball_y, -((BORDER_WIDTH /2 -  PADDLE_LENGTH * TURTLE_SIZE / 2)))
        self.teleport(RIGHT, pad_y)
        
    def reset(self):
        self.clear()