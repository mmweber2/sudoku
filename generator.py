from board import Board
from math import sqrt
import random

def generate(size=9):
    """Generates a new board of the given size.

    Args:
        size: integer, the length/width of the board. Must be a squared integer
            in the range 4 <= size <= 100.
            Example sizes include 4, 9, and 25.
            Defaults to 9, the standard sudoku board size.

    Raises:
        ValueError: size is not a valid board size.
    """
    if sqrt(size) not in (4, 9, 25, 36, 49, 64, 81, 100):
        raise ValueError("Board size must be a squared integer <= 100.")
    board_array = [[0] * size for _ in xrange(size)]
    board = Board(board_array)
    for row in xrange(size):
        for col in xrange(size):
            possible_moves = list(board.valid_moves(row, col))
            rand = random.randint(0, len(possible_moves) - 1)
            board.make_move(row, col, possible_moves[rand])

