from board import Board
import copy
from solver import fill_board
from solver import count_solutions
from math import sqrt
import random

def generate_puzzle():
    """Generates a new, ready to fill Board object.

    Returns:
        A randomly generated Board object with a unique solution.
    """
    board = generate_full_board()
    return remove_moves(board)

def generate_full_board():
    """Generates a new, completed board.

    Returns:
        A randomly generated, filled Board object.
    """
    # Randomly fill the first row, fill the rest, then make a transfomation
    first_row = random.sample(xrange(1, 10), 9)
    input_array = [first_row] + [([0] * 9) for _ in xrange(8)]
    return fill_board(Board(input_array))

def remove_moves(board):
    """Removes moves from board as long as there is only one valid solution."""
    # Generate 0-81 and shuffle them
    # According to the documentation, random.shuffle doesn't generate most permutations,
    #   but it should be enough to make it interesting.
    all_positions = range(81)
    random.shuffle(all_positions)
    # If removing a number creates more than one solution, it will only get worse
    #   as more numbers are removed, so don't try the same position twice.
    # Whether or not a number is removed, it should only be tried once.
    for position in all_positions:
        # Map full number to row, col pair
        c_row = position / 9
        c_col = position % 9
        answer_number = board.board[c_row][c_col]
        if answer_number == 0:
            # Nothing to remove at this position
            continue
        board_copy = copy.deepcopy(board)
        board_copy.board[c_row][c_col] = 0
        # Make a copy of the board because count_solutions modifies the board
        solution_count = count_solutions(copy.deepcopy(board_copy))
        # Solution count should never be 0
        if solution_count == 1:
            # Can't remove this number and maintain a unique board
            board = board_copy
            assert board.board[c_row][c_col] == 0
    return board

if __name__ == "__main__":
    #print generate_puzzle()
    puzzles = []
    for _ in xrange(1):
        puzzle = generate_puzzle()
        puzzles.append("".join(str(x) for row in puzzle.board for x in row))
    puzzles = "\n".join(puzzles)
    with open("puzzles.txt", "a") as fh:
        fh.write("\n")
        fh.write(puzzles)
        






