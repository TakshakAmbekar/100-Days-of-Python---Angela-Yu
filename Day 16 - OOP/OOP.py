'''
An object has attributes (the data it holds) and methods (what it can do)
Classes are named in Pascal case to differentiate them from variables and function
'''

from turtle import Turtle, Screen

# Constructing an Object
timmy = Turtle()     # Turtle is a class in turtle module
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()
