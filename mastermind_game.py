"""Play Mastermind by cracking a four-digit secret code."""

import random


CODE_LENGTH = 4
MAX_ATTEMPTS = 10
DIGITS = "0123456789"


def create_secret():
    """Return a code made of four distinct digits."""
    return "".join(random.sample(DIGITS, CODE_LENGTH))


def get_feedback(secret, guess):
    """Return counts of correctly placed and misplaced digits."""
    exact = sum(secret_digit == guess_digit for secret_digit, guess_digit in zip(secret, guess))
    misplaced = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess)) - exact
    return exact, misplaced


def play_game():
    """Run one round of Mastermind."""
    secret = create_secret()
    print("\n=== Mastermind ===")
    print(f"Crack the {CODE_LENGTH}-digit code. Digits do not repeat.")
    print(f"You have {MAX_ATTEMPTS} guesses. Feedback shows exact and misplaced digits.")

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        guess = input(f"\nGuess {attempts + 1}/{MAX_ATTEMPTS}: ").strip()
        if len(guess) != CODE_LENGTH or not guess.isdigit() or len(set(guess)) != CODE_LENGTH:
            print("Enter four different digits, from 0 to 9.")
            continue

        attempts += 1
        exact, misplaced = get_feedback(secret, guess)
        if exact == CODE_LENGTH:
            print(f"You cracked the code in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            return
        print(f"Exact: {exact} | Misplaced: {misplaced}")

    print(f"Out of guesses. The code was {secret}.")


def main():
    """Offer replay and exit options."""
    print("=== Mastermind ===")
    while True:
        print("\n1. Play")
        print("2. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Please enter 1 or 2.")


if __name__ == "__main__":
    main()