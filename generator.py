from board import Board
from solver import fill_board
from math import sqrt
import random

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
    # random.shuffle exists, but according to the documentation, it doesn't
    #   generate most permutations, so I use random.sample.
    all_positions = random.sample(range(81), 81)
    # If removing a number creates more than one solution, it will only get worse
    #   as more numbers are removed, so don't try the same position twice.
    # Whether or not a number is removed, it should only be tried once.
    tried_positions = set()
    while True:
        current = all_positions.pop()
        # Map full number to row, col pair
        c_row = current / 9
        c_col = current % 9
        answer_number = board[c_row][c_col]
        board[c_row][c_col] = 0
        if len(board.valid_moves(c_row, c_col)) == 1:
            # TODO
            pass

        






