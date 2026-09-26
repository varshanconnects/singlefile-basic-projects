# Coin Flip Challenge
# Guess heads or tails and try to beat the computer across several rounds!

import random


def flip_coin():
    """Return the result of a coin toss."""
    return random.choice(["heads", "tails"])


def play_round(score):
    """Play one round and return the updated score."""
    print("\nChoose: heads or tails")
    guess = input("Your call: ").strip().lower()

    if guess == "quit":
        print(f"Thanks for playing! Final score: {score}")
        return None

    if guess not in ["heads", "tails"]:
        print("Invalid choice! Please type 'heads' or 'tails'.")
        return score

    result = flip_coin()
    print(f"Coin landed on: {result}")

    if guess == result:
        score += 1
        print("You win this round! 🎉")
    else:
        print("The computer wins this round.")

    print(f"Current score: {score}")
    return score


def play_game():
    """Main loop for the Coin Flip game."""
    score = 0
    rounds = 0

    print("\n=== Welcome to Coin Flip Challenge ===")
    print("Type 'quit' at any time to stop playing.")

    while True:
        result = play_round(score)
        if result is None:
            return

        score = result
        rounds += 1

        if rounds >= 5:
            print(f"\nGame over! You scored {score} point(s) out of 5 rounds.")
            play_again = input("Play again? (y/n): ").strip().lower()
            while play_again not in ["y", "n"]:
                print("Please enter 'y' or 'n'.")
                play_again = input("Play again? (y/n): ").strip().lower()

            if play_again == "n":
                print("Thanks for playing!")
                return

            score = 0
            rounds = 0


def main():
    """Menu loop for the game."""
    print("=== Coin Flip Challenge ===")

    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()
