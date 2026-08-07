import random, os
from celebs import celebrities

def greet():
    print("Welcome to Higher-Lower!")

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def choose():
    '''Choose a random celebrity'''
    return random.choice(list(celebrities.keys()))


def display(first, second):
    '''Display both celebrity names'''
    print(f"\n1. {first}\n2. {second}")


def compare(first, second):
    '''Compare the followers of both celebs, return True if second celebrity has greater followers'''
    return celebrities[second] > celebrities[first]


def get_player_choice(first):
    '''Get the player's guess'''''''''''''''
    while True:
        choice = input(f"Press 1 if you think {first} is the winner, else press 2: ")

        if choice in ("1", "2"):
            return choice == "2"

        print("Invalid input. Please press 1 or 2.")


def play_round(first, score):
    '''Play one single round of guessing'''
    second = choose()
    while second == first:
        second = choose()
    
    display(first, second)
    
    answer = compare(first, second)
    guess = get_player_choice(first)
    clear()
    
    if answer == guess:
        score += 1
        print(f"Correct! Score: {score}")
        return second, score, True

    print("Wrong!")
    print(f"\n{first}: {celebrities[first]}M, {second}: {celebrities[second]}M")
    print(f"\nFinal score: {score}")
    return first, score, False


def main():
    '''Main'''
    new_game = True
    high_score = 0
    
    while new_game:
        first = choose()
        score = 0
        playing = True
        
        clear()
        greet()
        
        # Play a single game
        while playing:
            first, score, playing = play_round(first, score)
            high_score = max(high_score, score)
        
        # Let user start a new game
        play_more = input("Play another game? 'y' or 'n': ")
        while play_more not in ('y', 'n'):
            play_more = input("Please enter a valid input (y/n): ")
        new_game = play_more == 'y'
    
    clear()
    print(f"Your high score was: {high_score}\nSee you next time")


if __name__ == "__main__":
    main()