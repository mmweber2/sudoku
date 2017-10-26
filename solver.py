from collections import namedtuple
import copy

# A move has a row, column, and other options to play instead
Move = namedtuple('Move', 'row col options')


# TODO: Cache this and have board keep track of it?
def _find_empty_spots(board):
    spots = []
    for row in xrange(board.board_size):
        for col in xrange(board.board_size):
            if board.board[row][col] == 0:
                spots.append((row, col))
    return spots

# Recursive move searcher and implementer
 
 # TODO: Don't modify board here directly
# TODO: Split actual move making into separate program
# TODO: Rename to reflect searching, not making moves
# TODO: Fill boxes in order of constraints?
# TODO: Is it better to use recursion or a stack?
def fill_board(board):
    """
    Raises:
        ValueError: board is not winnable from the given position.
    """
    # Set a maximum value for moves remaining from a square
    smallest_move = float("inf")
    next_moves = []
    for row, col in _find_empty_spots(board):
        remaining = board.valid_moves(row, col)
        if not remaining:
            # Dead-end position
            return False
        elif len(remaining) == 1:
            # Make move and continue
            board[row][col] = remaining[0]
            return fill_board(board)
        else:
            # Find most constrained position, if no 1s or 0s
            if len(remaining) < smallest_move:
                smallest_move = len(remaining)
                next_moves.append(Move(row, col, remaining))
    # Check for won position
    if not next_moves and board._is_valid_board():
        return True
    # Otherwise, make one of the most constrained moves
    for move in next_moves:
        # These moves could be wrong, so make a copy of the board
        for option in move.options:
            board_copy = copy.deepcopy(board)
            board_copy[move.row][move.col] = option
            if fill_board(board_copy):
                return True
    return False