from collections import namedtuple
import copy

# A move has a row, column, and other options to play instead
Move = namedtuple('Move', 'row col options')

# TODO: Cache this and have board keep track of it?
def _find_empty_spots(board):
    spots = []
    for row in xrange(9):
        spots.extend([(row, col) for col in xrange(9) if not board.board[row][col]])
    return spots

def count_solutions(board):
    """
    Counts the number of solutions for this board, up to 2.

    If the count is 0, the board cannot be solved from the current configuration.

    This function aborts counting after 2 solutions are found.

    Returns:
        One of the integers 0, 1, or 2.
    """
    # For now, don't worry about finding most constrained position
    solutions = 0 # Put in scope for case where there are no solutions
    spots = _find_empty_spots(board)
    for row, col in _find_empty_spots(board):
        remaining = board.valid_moves(row, col)
        if not remaining:
            # Dead-end position
            return 0
        solutions = 0
        for move in remaining:
            # Try all of these moves
            # fill_board will attempt to complete the board, so copy it for future checks
            board_copy = copy.deepcopy(board)
            board_copy.board[row][col] = move
            if fill_board(board_copy):
                solutions += 1
                if solutions == 2:
                    return 2
    return solutions # Should be 0 or 1

# Recursive move searcher and implementer
# TODO: Is it better to use recursion or a stack?
def fill_board(board):
    """
    Fully solves the board, if possible, and returns the result.

    Returns:
        The solved board object if the board is solvable, None otherwise.
    """
    # Set a maximum value for moves remaining from a square
    smallest_move = float("inf")
    next_moves = []
    for row, col in _find_empty_spots(board):
        remaining = board.valid_moves(row, col)
        if not remaining:
            # Dead-end position
            return None
        elif len(remaining) == 1:
            # Make move and continue
            board.board[row][col] = remaining.pop()
            return fill_board(board)
        else:
            # Find most constrained position, if no 1s or 0s
            if len(remaining) < smallest_move:
                smallest_move = len(remaining)
                next_moves.append(Move(row, col, remaining))
    # Check for won position; board must be valid because moves were
    #   chosen only from valid moves
    if not next_moves:
        # Pass up the winning board
        return board
    # Otherwise, make one of the most constrained moves
    for move in next_moves:
        for option in move.options:
            board.board[move.row][move.col] = option
            # fill_board will attempt to fill the board passed to it.
            # If it's not successful, it will contain moves that don't lead to
            #   a valid solution, with no path to undoing them, so make a copy.
            end_result = fill_board(copy.deepcopy(board))
            # end_result will be None unless it is fully complete.
            if end_result:
                # Pass up the winning board
                return end_result
    return None