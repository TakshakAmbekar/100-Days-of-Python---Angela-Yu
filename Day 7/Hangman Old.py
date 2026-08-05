from random import choice
from Words import word_list

print("Welcome to Hangman")

chosen_word = choice(word_list)
length = len(chosen_word)
lives = 7

# print(chosen_word, "\n")

correct_guesses = []
wrong_guesses = []

for letter in chosen_word:
    correct_guesses.append("_")
    
display = ""
for c in correct_guesses:
    display += c

print(display)

game_over = False

while not game_over and lives > 0:
    print(f"You have {lives} lives left.")
    guess = input("Guess a letter: ").lower().strip()
    while len(guess) != 1:
        guess = input("Type in a single letter: ").lower().strip()
    
    found = False
    for i in range(length):
        if guess == chosen_word[i]:
            found = True
            correct_guesses[i] = guess 
    
    if not found:
        print("That was a wrong guess")
        if guess not in wrong_guesses:
            wrong_guesses.append(guess) 
            lives -= 1
            if lives == 0:
                game_over = True
    
    else:
        print("That was a right guess")
                
    display = ""
    for c in correct_guesses:
        display += c
    print(display, "\n")
    
    if "_" not in correct_guesses:
        game_over = True

if lives:
    print(f"You guessed the word {chosen_word} correctly!")
else:
    print(f"You lost! The word was {chosen_word}")

