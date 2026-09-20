"""Minesweeper played in the terminal."""

import random


DIFFICULTIES = {
    "1": ("Beginner", 8, 8, 10),
    "2": ("Intermediate", 10, 10, 18),
    "3": ("Expert", 12, 12, 30),
}


def neighbours(row, col, rows, cols):
    """Yield every valid square surrounding a position."""
    for row_change in (-1, 0, 1):
        for col_change in (-1, 0, 1):
            if row_change == 0 and col_change == 0:
                continue
            neighbour_row = row + row_change
            neighbour_col = col + col_change
            if 0 <= neighbour_row < rows and 0 <= neighbour_col < cols:
                yield neighbour_row, neighbour_col


def build_board(rows, cols, mine_count, safe_start, rng=None):
    """Return a board with mines placed away from the first square."""
    rng = rng or random
    safe_squares = {safe_start, *neighbours(*safe_start, rows, cols)}
    available = [
        (row, col)
        for row in range(rows)
        for col in range(cols)
        if (row, col) not in safe_squares
    ]
    if mine_count > len(available):
        raise ValueError("Too many mines for the selected board.")

    mines = set(rng.sample(available, mine_count))
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    for row, col in mines:
        board[row][col] = -1

    for row in range(rows):
        for col in range(cols):
            if board[row][col] != -1:
                board[row][col] = sum(
                    board[neighbour_row][neighbour_col] == -1
                    for neighbour_row, neighbour_col in neighbours(row, col, rows, cols)
                )
    return board


def reveal(board, visible, row, col):
    """Reveal a square and cascade through empty areas."""
    rows, cols = len(board), len(board[0])
    if visible[row][col] or board[row][col] == -2:
        return

    visible[row][col] = True
    if board[row][col] == 0:
        for neighbour_row, neighbour_col in neighbours(row, col, rows, cols):
            reveal(board, visible, neighbour_row, neighbour_col)


def render(board, visible, flags):
    """Return a printable view of the current board."""
    rows, cols = len(board), len(board[0])
    output = ["    " + " ".join(f"{col + 1:2}" for col in range(cols))]
    for row in range(rows):
        cells = []
        for col in range(cols):
            position = (row, col)
            if position in flags:
                cell = "F"
            elif not visible[row][col]:
                cell = "."
            elif board[row][col] == -1:
                cell = "*"
            else:
                cell = str(board[row][col])
            cells.append(f"{cell:2}")
        output.append(f"{row + 1:2}  " + " ".join(cells))
    return "\n".join(output)


def is_complete(board, visible, flags):
    """Return whether every non-mine square has been revealed."""
    for row, line in enumerate(board):
        for col, value in enumerate(line):
            if value != -1 and not visible[row][col]:
                return False
    return True


def get_move(rows, cols):
    """Read a move as `r c` or `f r c`, or return None to quit."""
    while True:
        command = input("Move (r c to reveal, f r c to flag, q to quit): ").strip().lower()
        if command == "q":
            return None

        parts = command.split()
        if len(parts) not in (2, 3) or (len(parts) == 3 and parts[0] != "f"):
            print("Use row and column, such as '2 4', or 'f 2 4' to flag.")
            continue

        try:
            row, col = (int(parts[-2]) - 1, int(parts[-1]) - 1)
        except ValueError:
            print("Rows and columns must be numbers.")
            continue

        if not (0 <= row < rows and 0 <= col < cols):
            print(f"Choose a row from 1-{rows} and a column from 1-{cols}.")
            continue
        return (row, col, len(parts) == 3)


def play_round(difficulty):
    """Play one round at the selected difficulty."""
    name, rows, cols, mine_count = difficulty
    first_move = True
    board = None
    visible = [[False] * cols for _ in range(rows)]
    flags = set()

    print(f"\n=== Minesweeper: {name} ===")
    print(f"Clear the board without hitting one of the {mine_count} mines.")

    while True:
        print("\n" + render(board, visible, flags) if board else "\n" + render(
            [[-2] * cols for _ in range(rows)], visible, flags
        ))
        move = get_move(rows, cols)
        if move is None:
            print("You left the minefield.")
            return False

        row, col, flagging = move
        position = (row, col)
        if flagging:
            if visible[row][col]:
                print("That square is already revealed.")
            elif position in flags:
                flags.remove(position)
                print("Flag removed.")
            elif len(flags) < mine_count:
                flags.add(position)
                print("Square flagged.")
            else:
                print("You cannot place more flags than there are mines.")
            continue

        if position in flags:
            print("Remove the flag before revealing this square.")
            continue

        if first_move:
            board = build_board(rows, cols, mine_count, position)
            first_move = False
        if board[row][col] == -1:
            for mine_row in range(rows):
                for mine_col in range(cols):
                    if board[mine_row][mine_col] == -1:
                        visible[mine_row][mine_col] = True
            print("\n" + render(board, visible, flags))
            print("\nBoom! You hit a mine.")
            return False

        reveal(board, visible, row, col)
        if is_complete(board, visible, flags):
            print("\n" + render(board, visible, flags))
            print("\nYou cleared the minefield. Well played!")
            return True


def choose_difficulty():
    """Return the selected difficulty settings."""
    while True:
        print("\nChoose a difficulty:")
        for key, settings in DIFFICULTIES.items():
            name, rows, cols, mines = settings
            print(f"{key}. {name} ({rows}x{cols}, {mines} mines)")
        choice = input("Enter choice (1/2/3): ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Please choose 1, 2, or 3.")


def main():
    """Run the Minesweeper menu."""
    print("=== Minesweeper ===")
    while True:
        print("\n1. Play\n2. Exit")
        choice = input("\nEnter choice (1/2): ").strip()
        if choice == "1":
            play_round(choose_difficulty())
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()
