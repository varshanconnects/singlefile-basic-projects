"""Classic Snake game played in the terminal."""

import os
import random

BOARD_WIDTH = 12
BOARD_HEIGHT = 12
DIRECTIONS = {
    "w": (-1, 0),
    "s": (1, 0),
    "a": (0, -1),
    "d": (0, 1),
}
OPPOSITE = {"w": "s", "s": "w", "a": "d", "d": "a"}


def clear_screen():
    """Clear the terminal output."""
    os.system("cls" if os.name == "nt" else "clear")


def generate_food(snake):
    """Return a random free grid cell for food."""
    free_cells = []
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if (row, col) not in snake:
                free_cells.append((row, col))

    if not free_cells:
        return None
    return random.choice(free_cells)


def draw_board(snake, food):
    """Print the board for the current snake position."""
    print("  " + " ".join(str(col) for col in range(BOARD_WIDTH)))
    for row in range(BOARD_HEIGHT):
        cells = []
        for col in range(BOARD_WIDTH):
            if (row, col) == snake[0]:
                cells.append("@")
            elif (row, col) in snake[1:]:
                cells.append("o")
            elif food is not None and (row, col) == food:
                cells.append("*")
            else:
                cells.append(".")
        print(f"{row} " + " ".join(cells))


def get_move(current_direction):
    """Read the player's next move and validate it."""
    while True:
        move = input("Move (W/A/S/D) or Q to quit: ").strip().lower()

        if move == "q":
            return None

        if move not in DIRECTIONS:
            print("Invalid move. Use W, A, S, or D.")
            continue

        if current_direction and OPPOSITE[move] == current_direction:
            print("You cannot move directly backwards.")
            continue

        return move


def play_game():
    """Run one game of Snake and return when the player quits or loses."""
    snake = [(BOARD_HEIGHT // 2, BOARD_WIDTH // 2), (BOARD_HEIGHT // 2, BOARD_WIDTH // 2 - 1)]
    current_direction = "d"
    food = generate_food(snake)
    score = 0

    print("\n=== Snake Game ===")
    print("Eat the food, grow longer, and avoid the walls and your own tail.")

    while True:
        clear_screen()
        print("=== Snake Game ===")
        print(f"Score: {score}")
        draw_board(snake, food)

        move = get_move(current_direction)
        if move is None:
            print("Thanks for playing!")
            return

        row_change, col_change = DIRECTIONS[move]
        new_head = (snake[0][0] + row_change, snake[0][1] + col_change)
        current_direction = move

        if not (0 <= new_head[0] < BOARD_HEIGHT and 0 <= new_head[1] < BOARD_WIDTH):
            print("Game over! You hit the wall.")
            return

        if new_head in snake:
            print("Game over! You ran into yourself.")
            return

        snake.insert(0, new_head)

        if food and new_head == food:
            score += 1
            if score >= 10:
                clear_screen()
                print("=== Snake Game ===")
                print(f"You win! Final score: {score}")
                draw_board(snake, food)
                return
            food = generate_food(snake)
        else:
            snake.pop()


def main():
    """Display the menu and allow repeated play sessions."""
    while True:
        clear_screen()
        print("\n=== Snake Game Menu ===")
        print("1. Play Snake")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_game()
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again != "y":
                print("Goodbye!")
                break
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Please choose 1 or 2.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
