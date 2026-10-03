# Arena Battle
# Fight your way through a pack of monsters, manage your health, and win the arena!

import random


class Player:
    def __init__(self):
        self.max_health = 20
        self.health = self.max_health
        self.attack_min = 4
        self.attack_max = 7
        self.heal_amount = 6
        self.block_amount = 3

    def attack(self):
        return random.randint(self.attack_min, self.attack_max)

    def heal(self):
        healed = random.randint(4, self.heal_amount)
        self.health = min(self.max_health, self.health + healed)
        return healed

    def block(self):
        return random.randint(0, self.block_amount)


class Monster:
    def __init__(self):
        self.name = random.choice([
            "Goblin",
            "Skeleton",
            "Slime",
            "Wolf",
            "Shadow Knight",
            "Stone Golem",
        ])
        self.max_health = 16
        self.health = self.max_health
        self.attack_min = 3
        self.attack_max = 8

    def attack(self):
        return random.randint(self.attack_min, self.attack_max)


def show_status(player, monster):
    print(f"\nPlayer: {player.health}/{player.max_health} HP")
    print(f"{monster.name}: {monster.health}/{monster.max_health} HP")


def monster_turn(player, monster, blocked):
    if monster.health <= 0:
        return

    damage = monster.attack()
    if blocked:
        damage = max(0, damage - blocked)

    player.health = max(0, player.health - damage)
    print(f"{monster.name} hits for {damage} damage.")

    if player.health == 0:
        print("You fall in battle. The arena wins this round.")


def battle_round(player, monster):
    while player.health > 0 and monster.health > 0:
        print("\nChoose your move:")
        print("1. Attack")
        print("2. Heal")
        print("3. Block")
        print("4. Run away")

        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice == "1":
            damage = player.attack()
            monster.health = max(0, monster.health - damage)
            print(f"You strike for {damage} damage!")
        elif choice == "2":
            healed = player.heal()
            print(f"You recover {healed} health.")
        elif choice == "3":
            blocked = player.block()
            print(f"You brace yourself and reduce the next attack by up to {blocked} damage.")
            monster_turn(player, monster, blocked)
            continue
        elif choice == "4":
            print("You retreat from the arena.")
            return "run"
        else:
            print("Invalid choice. Try again.")
            continue

        if monster.health <= 0:
            print(f"You defeat the {monster.name}!")
            return "win"

        monster_turn(player, monster, 0)

        if player.health <= 0:
            print(f"The {monster.name} defeats you.")
            return "lose"

        show_status(player, monster)

    return "lose" if player.health <= 0 else "win"


def play_game():
    player = Player()
    wins = 0
    rounds = 0

    print("\n=== Arena Battle ===")
    print("Survive as many monsters as you can in the arena.")

    while rounds < 3 and player.health > 0:
        rounds += 1
        monster = Monster()
        print(f"\nRound {rounds}: A wild {monster.name} appears!")

        result = battle_round(player, monster)

        if result == "run":
            print("You escaped the arena with your pride intact.")
            break

        if result == "win":
            wins += 1
            print(f"Victory! You have defeated {wins} monster(s).")
        else:
            print("Your adventure ends here.")
            break

        if player.health <= 0:
            break

        print("You take a breath before the next fight...")

    if player.health > 0 and wins >= 3:
        print("\nYou are the champion of the arena!")
    elif player.health > 0:
        print(f"\nYou survived the arena and won {wins} round(s).")
    else:
        print("\nThe arena claims another challenger.")

    play_again = input("Play again? (y/n): ").strip().lower()
    while play_again not in ["y", "n"]:
        print("Please enter 'y' or 'n'.")
        play_again = input("Play again? (y/n): ").strip().lower()

    return play_again == "y"


def main():
    print("=== Arena Battle ===")

    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. Exit")

        choice = input("Enter choice (1/2): ").strip()

        if choice == "1":
            if not play_game():
                print("Goodbye!")
                break
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
