# Cows and Bulls
# Crack the hidden 4-digit code by testing your deduction skills.

import random


def generate_secret(length=4):
    """Return a unique secret code with no repeated digits."""
    digits = list("0123456789")
    return "".join(random.sample(digits, length))


def evaluate_guess(secret, guess):
    """Return bulls and cows for a guess compared to the secret code."""
    bulls = 0
    cows = 0

    for index, digit in enumerate(guess):
        if digit == secret[index]:
            bulls += 1
        elif digit in secret:
            cows += 1

    return bulls, cows


def play_game():
    """Run a full game of Cows and Bulls."""
    secret = generate_secret()
    max_guesses = 10

    print("\n=== Welcome to Cows and Bulls ===")
    print(f"Try to guess the {len(secret)}-digit secret code.")
    print("- Bulls = correct digit in the correct position")
    print("- Cows = correct digit in the wrong position")
    print(f"You have {max_guesses} guesses to crack it!\n")

    for turn in range(1, max_guesses + 1):
        while True:
            guess = input(f"Turn {turn}/{max_guesses} - Enter your guess: ").strip()
            if guess.isdigit() and len(guess) == len(secret):
                break
            print(f"Please enter a {len(secret)}-digit number using digits 0-9.")

        bulls, cows = evaluate_guess(secret, guess)
        print(f"Result: {bulls} bull(s), {cows} cow(s)")

        if bulls == len(secret):
            print(f"\n🎉 You cracked the code! The secret was {secret}.")
            return

    print(f"\n💥 You ran out of guesses! The secret code was {secret}.")


def main():
    """Menu loop for the game."""
    print("=== Cows and Bulls ===")

    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()
