import random

EASY_LIVES = 10
HARD_LIVES = 7
LOWEST = 1
HIGHEST = 100


def get_lives():
    """Ask the user to choose a difficulty."""
    while True:
        difficulty = input("Choose difficulty (1 = Easy, 2 = Hard): ")

        if difficulty == "1":
            return EASY_LIVES
        elif difficulty == "2":
            return HARD_LIVES

        print("Invalid choice. Please enter 1 or 2.\n")


def get_guess():
    """Get a valid guess from the user."""
    while True:
        try:
            guess = int(input(f"Guess a number ({LOWEST}-{HIGHEST}): "))

            if LOWEST <= guess <= HIGHEST:
                return guess

            print(f"Please enter a number between {LOWEST} and {HIGHEST}.")

        except ValueError:
            print("Please enter a valid integer.")


def compare(guess, answer):
    """Compare the guess with the answer."""

    if guess < answer:
        print("Too low. Go higher!")
        return False

    if guess > answer:
        print("Too high. Go lower!")
        return False

    print(f"Correct! The number was {answer}.")
    return True


def play_game():
    answer = random.randint(LOWEST, HIGHEST)
    lives = get_lives()

    print(f"\nI'm thinking of a number between {LOWEST} and {HIGHEST}.")

    while lives > 0:
        print(f"\nLives remaining: {lives}")

        guess = get_guess()

        if compare(guess, answer):
            return

        lives -= 1

    print(f"\nYou ran out of lives. The number was {answer}.")


def main():
    print("===== Number Guessing Game =====")

    while True:
        play = input("\nPlay a game? (y/n): ").lower()

        if play != "y":
            print("Thanks for playing!")
            break

        play_game()


if __name__ == "__main__":
    main()