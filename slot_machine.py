# Slot Machine
# Spin the reels, place a bet, and try to beat the house.

import random


SYMBOLS = ["Cherry", "Carrot", "Ball", "Bar", "Seven"]


def spin_reels():
    """Return a random set of three slot symbols."""
    return [random.choice(SYMBOLS) for _ in range(3)]


def score_result(reels, bet):
    """Return the payout amount for a spin."""
    first, second, third = reels

    if first == second == third:
        if first == "Seven":
            return bet * 20
        return bet * 5

    if first == second or second == third or first == third:
        return bet * 2

    return 0


def display_reels(reels):
    """Display the current slot reel results."""
    print(" | ".join(reels))


def play_round(balance):
    """Play a single round and return the updated balance."""
    while True:
        try:
            bet = int(input(f"How much would you like to bet? (1-{balance} or 0 to quit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if bet == 0:
            print("Thanks for playing!")
            return balance, False

        if 1 <= bet <= balance:
            break

        print(f"Your bet must be between 1 and {balance}.")

    reels = spin_reels()
    print("Reels:")
    display_reels(reels)

    payout = score_result(reels, bet)
    if payout > 0:
        print(f"Winner! You won ${payout}.")
        balance += payout
    else:
        print(f"No match this time. You lost ${bet}.")
        balance -= bet

    print(f"Current balance: ${balance}")
    return balance, True


def main():
    """Run the slot machine game."""
    print("=== Slot Machine ===")
    print("Match symbols to win credits. Try to cash out before you run out!")

    balance = 100

    while True:
        print("\nMenu:")
        print("1. Play a round")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            balance, keep_playing = play_round(balance)
            if balance <= 0:
                print("You are out of credits. Game over!")
                break
            if not keep_playing:
                break
        elif choice == "2":
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
