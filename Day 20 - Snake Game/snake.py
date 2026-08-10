from turtle import Turtle, Screen
import time

SPEED = 1


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.speed(SPEED)
        self.teleport(200, 300)
        
    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", font = ("Arial", 10, "normal"))

# Display nom nom nom when eating
class Comment(ScoreBoard):
    def __init__(self):
        super().__init__()
        self.teleport(0, 250)
        self.running = False
    
    def display(self):
        self.count = 0
        self.running = True
        self.words = ""
        self.animate()

    def animate(self):
        self.clear()

        if self.running:
            if self.count < 7:
                self.words += "NOM "
                self.write(self.words, align="center")
                self.count += 1
                self.getscreen().ontimer(self.animate, 200)
            elif self.count == 7:
                self.words += "NOM..."
                self.write(self.words, align="center")
                self.count += 1
                self.getscreen().ontimer(self.clear, 500)
                self.running = False
    
    def stop(self):
        self.running = False
        self.clear()


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
        self.scoreboard = ScoreBoard()
        self.scoreboard.score = 0
        self.scoreboard.display()   
        self.comment = Comment() 
        self.game_over_comment = Comment()
        
        
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
    
    def move(self, food, create_food):
        snake = self.snake
        length = len(snake)
        for i in range(length - 1, 0, -1):
            x, y = snake[i - 1].position()
            snake[i].teleport(x, y)
        self.head.forward(20)
        self.distance(food, create_food)
    
    def grow(self):
        self.scoreboard.score += 1
        self.scoreboard.display()
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
        self.comment.display()
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

    def game_over(self, screen):
        screen.clear()
        self.comment.stop()
        self.game_over_comment.teleport(0,0)
        self.game_over_comment.write("GAME OVER", align = "center", font = ("Arial", 40, "bold"))
        self.game_over_comment.teleport(0, -30)
        self.game_over_comment.write("Press space to play again", align = "center", font = ("Arial", 10, "italic"))
        