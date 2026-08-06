# There is no block scope in python
game_level = 3

if game_level < 5:
    new_enemy = "Zombie"
 
print(new_enemy)        # prints "Zombie" because there is not block scope in python




# Local Scope
enemies = 1

def increase_enemies():
    enemies = 2     # this is a different variable that the enemies variable declared before
    print(f"Enemies inside function: {enemies}")
    
increase_enemies()  # prints 2

print(f"Enemies outside function: {enemies}")   # prints 1



def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)      # raises NameError since potion_strength only exists in scope of drink_potion function



# Global Scope
health = 100
def fun1():
    print(health)       # prints 100
fun1()

def fun2():
    # health += 10      # UnboundLocalError: cannot access local variable 'health' where it is not associated with a value
    global health       # explicitly tell function to use global variable
    health += 10
    print(health)       
fun2()

print(health)
