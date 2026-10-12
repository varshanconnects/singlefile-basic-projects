# Snake Game
# Guide the snake, eat the apples, and grow as long as you can without crashing.

import os
import random
import time

try:
    import msvcrt
except ImportError:
    msvcrt = None

BOARD_WIDTH = 15
BOARD_HEIGHT = 15
INITIAL_SNAKE = [(5, 7), (4, 7), (3, 7)]
DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
}


def clear_screen():
    """Clear the terminal window."""
    os.system("cls" if os.name == "nt" else "clear")


def create_food(snake):
    """Create a food position that is not on the snake."""
    available = []
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if (col, row) not in snake:
                available.append((col, row))
    return random.choice(available) if available else None


def draw_board(snake, food, score):
    """Render the current game board."""
    clear_screen()
    print("=== Snake Game ===")
    print(f"Score: {score}")
    print("Controls: W/A/S/D to move, Q to quit")
    print()

    for row in range(BOARD_HEIGHT):
        line = []
        for col in range(BOARD_WIDTH):
            position = (col, row)
            if position == food:
                line.append("@")
            elif position in snake:
                if position == snake[0]:
                    line.append("O")
                else:
                    line.append("o")
            else:
                line.append(" ")
        print("|" + " ".join(line) + "|")
    print("-" * (BOARD_WIDTH * 2 + 1))


def get_key_direction(key, current_direction):
    """Convert keyboard input into movement direction."""
    key = key.lower()
    directions = {
        "w": "UP",
        "s": "DOWN",
        "a": "LEFT",
        "d": "RIGHT",
    }

    if key in directions:
        next_direction = directions[key]
        delta_x, delta_y = DIRECTIONS[next_direction]
        current_dx, current_dy = DIRECTIONS[current_direction]
        if (delta_x, delta_y) != (-current_dx, -current_dy):
            return next_direction
    return current_direction


def read_key():
    """Read a single key press for Windows or Unix systems."""
    if msvcrt is not None:
        if msvcrt.kbhit():
            key = msvcrt.getwch()
            return key
        return None

    import sys
    import termios
    import tty

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        key = sys.stdin.read(1)
        return key
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def play_game():
    """Run the Snake game loop."""
    snake = INITIAL_SNAKE[:]
    direction = "RIGHT"
    food = create_food(snake)
    score = 0
    game_over = False

    if food is None:
        print("Board is full. There is no room for food.")
        return

    while not game_over:
        draw_board(snake, food, score)

        key = read_key()
        if key:
            if key.lower() == "q":
                print("\nYou quit the game. Thanks for playing!")
                return
            direction = get_key_direction(key, direction)

        head_x, head_y = snake[0]
        delta_x, delta_y = DIRECTIONS[direction]
        new_head = (head_x + delta_x, head_y + delta_y)

        if (
            new_head[0] < 0
            or new_head[0] >= BOARD_WIDTH
            or new_head[1] < 0
            or new_head[1] >= BOARD_HEIGHT
            or new_head in snake[:-1]
        ):
            game_over = True
            continue

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            food = create_food(snake)
            if food is None:
                print("\nYou ate every available space! You win!")
                return
        else:
            snake.pop()

        time.sleep(0.18)

    print("\nGame over! Final score:", score)
    print("Press Enter to return to the menu.")
    input()


def main():
    """Menu loop for the Snake game."""
    while True:
        clear_screen()
        print("=== Snake Game ===")
        print("1. Play")
        print("2. Exit")
        choice = input("Enter choice (1/2): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1 or 2.")
            time.sleep(1)


if __name__ == "__main__":
    main()
