from collections import namedtuple

# A move has a row, column, and other options to play instead
Move = namedtuple('Move', 'row col options')


def _find_empty_spot(board):
    for row in xrange(board.board_size):
        for col in xrange(board.board_size):
            if board.board[row][col] == 0:
                return (row, col)
    # Board is full
    return None

# Recursive move searcher and implementer
 
 # TODO: Don't modify board here directly
# TODO: Split actual move making into separate program
# TODO: Rename to reflect searching, not making moves
# TODO: Fill boxes in order of constraints?
def fill_board(board):
    """
    Raises:
        ValueError: board is not winnable from the given position.
    """
    # Previous moves made for backtracking
    move_stack = []
    # Indices of current position
    row = 0
    col = 0
    # TODO
    # Move this out into a separate function
    while True:
        # Set a maximum value for moves remaining from a square
        smallest_move = float("inf")
        value_to_put = 0
        next_move = None
        # Skip filled positions
        if board.board[row][col] != 0:
            col += 1
            if col == board.board_size:
                # Reached end of row
                col = 0
                row += 1
            if row == board.board_size:
                # Reached end of board
                break
            continue
        remaining = board.valid_moves(row, col)
        if not remaining:
            # Dead-end position
            # Undo all moves after the last move with other options
            while move_stack and move_stack[-1].options:
                last_move = move_stack.pop()
                board.board[last_move.row][last_move.col] = 0
            if not move_stack:
                # No moves with options have been made; invalid board
                raise ValueError("No valid moves for ({},{})".format(row, col))
            # Try another move from the last position with options
            last_move = move_stack.pop()
            row, col = last_move.row, last_move.col
            # Take the next value from the option list and try that
            value_to_put = last_move.options.pop(0)
            move_stack.append(Move(row, col, last_move.options))
            next_move = (row, col, value_to_put)
        elif len(remaining) == 1:
            # Make move and continue
            assert board.make_move(row, col, remaining.pop())
        else:
        # TODO: Move
        # random.shuffle(remaining)
            # Find most constrained position, if no 1s or 0s
            if len(remaining) < smallest_move:
                smallest_move = len(remaining)
                next_move = (row, col, remaining.pop())
        if next_move is None and board._is_valid_board():
            return board.board
        # Make move
    # TODO: Pick up here
    # Check for won position
        i, j = next_move[0], next_move[1]
        for move in next_move[2]:
            assert board.make_move(i, j, move)
            # Pass up the board if we found a winning position
            else: return board
        return None