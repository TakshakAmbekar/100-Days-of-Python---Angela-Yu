import random

print(random.randrange(-10, 100, 5))    # Generates random integer in range [-10, 100) in steps of 5 starting at -10

print(random.randrange(10))         # Assumes start = 0, stop = 10, step = 1

print(random.randint(-10, 10))    # Random integer in [-10, 10]

print(random.random())      # float in [0.0, 1.0)

print(random.uniform(10,100))   # float in [10, 100]

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)