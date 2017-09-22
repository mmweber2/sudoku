# Recursive move searcher and implementer
 
 # TODO: Don't modify board here directly
# TODO: Split actual move making into separate program
# TODO: Rename to reflect searching, not making moves
def find_moves_recursive(board):
    smallest_move = board.board_size + 1
    for i in xrange(board.board_size):
        for j in xrange(board.board_size):
            # Skip filled positions
            if board.board[i][j] != 0:
                continue
            remaining = board.valid_moves(i, j)
            # Dead-end position, so end this recursion
            if len(remaining) == 0:
                return None
            if len(remaining) == 1:
                # Make move and recurse
                board_copy = board.board.copy()
                board_copy[i][j] = remaining.pop()
                return make_moves(board_copy)
            else:
                # Find most constrained position, if no 1s or 0s
                if len(remaining) < smallest_move:
                    smallest_move = len(remaining)
                    next_move = (i, j, remaining)
        # Check for won position
        if next_move == None:
            if board._is_valid_board():
                return board.board
        i, j = next_move[0], next_move[1]
        for move in next_move[2]:
            board.board[i][j] = move
            board_result = make_moves(board)
            if board_result == None:
                board.board[i][j] = 0
            # Pass up the board if we found a winning position
            else: return board_result
        return None