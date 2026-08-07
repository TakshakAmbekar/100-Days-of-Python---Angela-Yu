from random import choice

order = ["rock", "paper", "scissors"]   # modulo 3: 0, 1, 2

print("Welcome to rock, paper, scissors\n")

player = input("Enter your choice: rock, paper, or scissors\n").lower()
print()

computer = choice(order)

# win = False
# tie = False

# if player == computer:
#     tie = True
# elif (player == "rock" and computer == "scissors") or (player == "rock" and computer == "scissors") or (player == "rock" and computer == "scissors"):
#     win = True
# else:
#     win = False

# if win:
#     print("You won")
# elif tie:
#     print("It was a tie")
# else:
#     print("You lost")
    

ci = order.index(computer)

if order.__contains__(player):
    pi = order.index(player)
    print(f"Computer played {computer}")
    if pi == ci:
        print("It was a tie")
    elif pi - ci == 1 or pi - ci == -2:
        print("You won")
    else:
        print("You lost")
else:
    print("Invalid Choice")