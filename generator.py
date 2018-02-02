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
    # Randomly fill the first row, then fill the rest
    first_row = random.sample(xrange(1, 10), 9)
    input_array = [first_row] + [([0] * 9) for _ in xrange(8)]
    return fill_board(Board(input_array))

def remove_moves(board):
    """Removes moves from board as long as there is only one valid solution."""
    # Generate 0-81 and shuffle them so that the open spaces aren't all in the top
    # According to the documentation, random.shuffle doesn't generate most permutations,
    #   but it should be enough to make it interesting.
    all_positions = range(81)
    random.shuffle(all_positions)
    # If removing a number creates more than one solution, it will only get worse
    #   as more numbers are removed, so don't try the same position twice.
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

def rotate_board(board_array):
    """Rotates a single board array to make three more board arrays.

    Rotates board_array by 90, 180, and 270 degrees to create 3 variants
        of the board array.
    """
    rotations = []
    for _ in xrange(3): # Rotate 3 times; 4th rotation is the original array
        half_size = 5 # 9 arrays, up to (not including) row 5
        for first in xrange(half_size):
            last = 8 - first # 9 - 1 - first
            for layer in xrange(first, last):
                offset = layer - first # How far in is this layer?
                top = board_array[first][layer] # Copy the top layer
                board_array[first][layer] = board_array[last-offset][first]
                board_array[last-offset][first] = board_array[last][last-offset]
                board_array[last][last-offset] = board_array[layer][last]
                board_array[layer][last] = top
        # Further rotations will change the array, so copy this version
        rotations.append(copy.deepcopy(board_array))
    return rotations

if __name__ == "__main__":
    puzzles = []
    for _ in xrange(1):
        puzzle = generate_puzzle()
        puzzles.append("".join(str(x) for row in puzzle.board for x in row))
    puzzles = "\n".join(puzzles)
    with open("puzzles.txt", "a") as fh:
        fh.write("\n")
        fh.write(puzzles)
        






