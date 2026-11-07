"""Play a terminal version of the Lights Out puzzle."""

import random


BOARD_SIZE = 5
MOVE_LIMIT = 35


def toggle_cross(board, row, col):
    """Toggle a cell and its orthogonal neighbors."""
    for row_change, col_change in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
        next_row = row + row_change
        next_col = col + col_change
        if 0 <= next_row < BOARD_SIZE and 0 <= next_col < BOARD_SIZE:
            board[next_row][next_col] = not board[next_row][next_col]


def make_puzzle():
    """Create a solvable board by scrambling a solved board."""
    board = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    scramble_moves = random.randint(12, 20)

    for _ in range(scramble_moves):
        toggle_cross(
            board,
            random.randrange(BOARD_SIZE),
            random.randrange(BOARD_SIZE),
        )

    if not any(any(row) for row in board):
        toggle_cross(board, random.randrange(BOARD_SIZE), random.randrange(BOARD_SIZE))

    return board


def print_board(board):
    """Display the puzzle with one-based row and column labels."""
    print("\n    " + "   ".join(str(col + 1) for col in range(BOARD_SIZE)))
    print("  +" + "---+" * BOARD_SIZE)
    for row_index, row in enumerate(board, start=1):
        cells = "".join(" ON |" if is_on else "    |" for is_on in row)
        print(f"{row_index} |{cells}")
        print("  +" + "---+" * BOARD_SIZE)


def is_solved(board):
    """Return True when every light is off."""
    return not any(any(row) for row in board)


def play_round():
    """Run one puzzle round and return when it is won or abandoned."""
    board = make_puzzle()
    moves = 0

    print("\n=== Lights Out ===")
    print("Turn every light off. Each move toggles a cell and its neighbors.")
    print(f"Enter row and column from 1 to {BOARD_SIZE}, or Q to quit this round.")

    while moves < MOVE_LIMIT:
        print_board(board)
        print(f"Moves: {moves}/{MOVE_LIMIT}")
        entry = input("Choose a cell (row column): ").strip().lower()

        if entry == "q":
            print("Round ended. The puzzle is ready whenever you are!")
            return

        parts = entry.split()
        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            print("Please enter two numbers, such as 2 4, or Q to quit.")
            continue

        row, col = (int(part) - 1 for part in parts)
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            print(f"Rows and columns must be between 1 and {BOARD_SIZE}.")
            continue

        toggle_cross(board, row, col)
        moves += 1

        if is_solved(board):
            print_board(board)
            print(f"You did it in {moves} moves! All lights are out.")
            return

    print_board(board)
    print("Move limit reached. Give it another try!")


def main():
    """Show the menu and allow the player to replay."""
    print("Welcome to Lights Out!")
    while True:
        choice = input("\n1. Play\n2. Exit\nChoose an option: ").strip()
        if choice == "1":
            play_round()
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()