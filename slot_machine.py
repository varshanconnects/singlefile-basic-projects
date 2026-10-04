import random


SYMBOLS = ["7", "BAR", "cherry", "bell", "star"]


def spin_reel():
    return random.choice(SYMBOLS)


def evaluate_spin(reels):
    first, second, third = reels
    if first == second == third == "7":
        return 10
    if first == second == third:
        return 5
    if first == second or second == third or first == third:
        return 2
    return 0


def show_reels(reels):
    print(" | ".join(reels))


def prompt_user(prompt):
    try:
        return input(prompt).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return "q"


def play_round(balance):
    print(f"\nCurrent balance: {balance} credits")
    bet = prompt_user("Place your bet (1-10, or 'q' to quit): ")

    if bet == "q":
        print("Thanks for playing!")
        return None

    try:
        bet_amount = int(bet)
    except ValueError:
        print("Please enter a number from 1 to 10, or 'q' to quit.")
        return balance

    if not 1 <= bet_amount <= 10:
        print("Bet must be between 1 and 10.")
        return balance

    if bet_amount > balance:
        print("You do not have enough credits for that bet.")
        return balance

    reels = [spin_reel() for _ in range(3)]
    print("Your spin:")
    show_reels(reels)

    payout_multiplier = evaluate_spin(reels)
    if payout_multiplier == 0:
        balance -= bet_amount
        print(f"No match this time. You lose {bet_amount} credits.")
    else:
        winnings = bet_amount * payout_multiplier
        balance += winnings
        print(f"Jackpot! You win {winnings} credits.")

    print(f"Balance: {balance} credits")
    return balance


def main():
    print("=== SLOT MACHINE ===")
    print("Match 3 symbols to win. A 7 triple pays 10x, any triple pays 5x, and pairs pay 2x.")

    balance = 20

    while True:
        if balance <= 0:
            print("You are out of credits. Thanks for playing!")
            return

        result = play_round(balance)
        if result is None:
            print(f"Final balance: {balance} credits")
            return

        balance = result

        if balance == 0:
            print("You are out of credits. Thanks for playing!")
            return

        again = prompt_user("Spin again? (y/n): ")
        if again not in {"y", "yes"}:
            print(f"Thanks for playing! Final balance: {balance} credits")
            return


if __name__ == "__main__":
    main()
