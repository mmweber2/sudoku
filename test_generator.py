from generator import generate_full_board
from generator import remove_moves

def is_full(board):
    for row in board.board:
        if 0 in row:
            return False
    return True

def test_generate_puzzle():
    for _ in xrange(20):
        # fill_board already checks validity, so just check that it is full
        b = generate_full_board()
        assert is_full(b)
        ready = remove_moves(b)
        assert ready is not None
