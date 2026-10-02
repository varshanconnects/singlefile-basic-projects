"""Maze Escape

A small terminal-based game where the player must collect a key and then
reach the exit before running out of moves.
"""

MAZE = [
    "#########",
    "#.......#",
    "#.......#",
    "#.......#",
    "#.......#",
    "#.......#",
    "#.......#",
    "#.......#",
    "#########",
]

PLAYER_START = (1, 1)
KEY_POSITION = (3, 3)
EXIT_POSITION = (5, 7)
MAX_MOVES = 25


def print_maze(player_row, player_col, has_key, moves_left):
    """Display the maze with the player and item markers."""
    for row_index, row in enumerate(MAZE):
        line = ""
        for col_index, cell in enumerate(row):
            if (row_index, col_index) == (player_row, player_col):
                line += "P"
            elif (row_index, col_index) == KEY_POSITION:
                line += "K" if not has_key else "."
            elif (row_index, col_index) == EXIT_POSITION:
                line += "E"
            else:
                line += cell
        print(line)
    print(f"Moves left: {moves_left}")
    if has_key:
        print("You have the key! Head to the exit.")
    else:
        print("Find the key to unlock the exit.")


def is_open_cell(row, col):
    """Check whether the target cell is inside the maze and not a wall."""
    if row < 0 or col < 0:
        return False
    if row >= len(MAZE) or col >= len(MAZE[0]):
        return False
    return MAZE[row][col] != "#"


def move_player(player_row, player_col, direction, has_key, moves_left):
    """Attempt to move the player in a direction and return updated state."""
    directions = {
        "w": (-1, 0),
        "a": (0, -1),
        "s": (1, 0),
        "d": (0, 1),
    }

    if direction not in directions:
        return player_row, player_col, has_key, moves_left, "invalid"

    row_change, col_change = directions[direction]
    next_row = player_row + row_change
    next_col = player_col + col_change

    if not is_open_cell(next_row, next_col):
        print("You can't go that way. There is a wall.")
        return player_row, player_col, has_key, moves_left, "blocked"

    player_row, player_col = next_row, next_col
    moves_left -= 1

    if (player_row, player_col) == KEY_POSITION:
        has_key = True
        print("You found the key! The exit is now unlocked.")

    if (player_row, player_col) == EXIT_POSITION:
        if has_key:
            print("You escaped the maze! You win!")
            return player_row, player_col, has_key, moves_left, "win"
        print("The exit is locked. You need the key first.")

    return player_row, player_col, has_key, moves_left, "ok"


def play_game():
    """Run the main game loop."""
    player_row, player_col = PLAYER_START
    has_key = False
    moves_left = MAX_MOVES

    print("=== Maze Escape ===")
    print("Collect the key, then reach the exit before your moves run out.")
    print("Controls: w = up, a = left, s = down, d = right, q = quit")

    while True:
        print_maze(player_row, player_col, has_key, moves_left)

        if moves_left <= 0:
            print("You ran out of moves. Game over!")
            break

        move_choice = input("Choose a direction: ").strip().lower()

        if move_choice == "q":
            print("You quit the maze. Better luck next time!")
            break

        player_row, player_col, has_key, moves_left, result = move_player(
            player_row, player_col, move_choice, has_key, moves_left
        )

        if result == "win":
            break

        if result == "invalid":
            print("Invalid move. Use w, a, s, d, or q.")


def main():
    """Entry point for the game."""
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
