from random import choice
from Words import word_list

import os

chosen_word = choice(word_list)
length = len(chosen_word)
lives = 7

correct_guesses = []
wrong_guesses = []

for letter in chosen_word:
    correct_guesses.append("_")

game_over = False
message = ""

while not game_over and lives > 0:
    os.system('cls')

    print("Welcome to Hangman", "\n")
    
    display = ""
    for c in correct_guesses:
        display += c
    print("Guess this word: ", display)
    
    if message:
        print(message)
    print(f"You have {lives} lives left.\n")
    
    

    guess = input("Guess a letter: ").lower().strip()
    while len(guess) != 1:
        guess = input("Type in a single letter: ").lower().strip()
    
    found = False
    for i in range(length):
        if guess == chosen_word[i]:
            found = True
            correct_guesses[i] = guess 
    
    if not found:
        message = f"'{guess}' was a wrong guess"
        if guess not in wrong_guesses:
            wrong_guesses.append(guess) 
            lives -= 1
            if lives == 0:
                game_over = True
    else:
        message = f"'{guess}' was a right guess"
    
    display = ""
    for c in correct_guesses:
        display += c
    print(display, "\n")
    
    if "_" not in correct_guesses:
        game_over = True

os.system("cls")

if lives:
    print(f"\nYou guessed the word '{chosen_word}' correctly!")
else:
    print(f"\nYou lost! The word was '{chosen_word}'")