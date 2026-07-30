print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
decision1 = input("Type 'left' or 'right'\n").lower()
print()

if decision1 != "left":
    print("You fell in a hole. Game over!")
else:
    print("You've come to a lake. Ther is an island in the middle of the lake.")
    decision2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    print()

    if decision2 != "wait":
        print("Game over")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.\n"
              "One red, one yellow, and one blue. Which one do you choose?")
        decision3 = input("Type 'red', 'yellow' or 'blue'\n").lower()
        print()

        if decision3 != 'red':
            if decision3 == 'yellow':
                print("The room caught on fire. Game Over!")
            else:
                print("You were attacked by angry beast. Game Over!")
        else:
            print("Congratulation! You found the treasure!")
