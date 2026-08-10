from turtle import Turtle

score_keeper = Turtle()
score_keeper.hideturtle()
score_keeper.penup()
score_keeper.setposition(300, 350)


DELTA = {
    0: (20, 0),
    90: (0, 20),
    180: (-20, 0),
    270: (0, -20)
}

SPEED = 1


# Inherit Segment from Turtle class
class Segment(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black", "red")
        self.shape("square")
        self.speed(SPEED)

class Snake():
    def __init__(self):
        self.snake = []
        self.score = 0
        
        score_keeper.write(f"Score: {self.score}")
        
        for i in range(3):
            segment = Segment()
            if i == 0:
                segment.color("black", "black")
            segment.teleport(i * -20 + 10, 10)
            self.snake.append(segment)
            
            self.head = self.snake[0]
        
    
    # Snake Methods
    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def move(self):
        snake = self.snake
        length = len(snake)
        for i in range(length - 1, 0, -1):
            x, y = snake[i - 1].position()
            snake[i].teleport(x, y)
        self.head.forward(20)
    
    def grow(self):
        self.score += 1
        score_keeper.clear()
        score_keeper.write(f"Score: {self.score}")
        tail = self.snake[-1]
        tail_x, tail_y = tail.position()
        
        segment = Turtle()
        segment.speed(SPEED)
        segment.shape("square")
        segment.color("black", "red")
        segment.penup()
        
        # delta_x, delta_y = DELTA[tail_heading]
        # segment.teleport(tail_x - delta_x, tail_y - delta_y)
        segment.teleport(tail_x, tail_y)
        self.snake.append(segment)
        
    def distance(self,food, create_food):
        if self.head.distance(food) <= 10:
            self.eat(create_food)
        
    def eat(self,create_food):
        self.grow()
        create_food(self)
    
    def busted(self):
        segment_positions = []
        for segment in self.snake:
            segment_positions.append(segment.position())
        x, y = self.head.position()
        border = 280
        if self.head.position() in segment_positions[1:]:
            return True
        if -border < x < border and -border < y < border:
            return False
        return True
        