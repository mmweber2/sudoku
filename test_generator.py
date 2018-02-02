from nose.tools import assert_equals
from generator import generate_full_board
from generator import remove_moves
from generator import generate_puzzle
from generator import rotate_board
import board

def is_full(board):
    for row in board.board:
        if 0 in row:
            return False
    return True

def test_generate_full_board():
    b = generate_full_board()
    # fill_board already checks validity, so just check that it is full
    assert is_full(b)

def test_remove_moves_from_full():
    full_board = board.Board([
                       [8, 6, 5, 7, 2, 9, 4, 3, 1],
                       [3, 1, 2, 6, 4, 8, 9, 7, 5],
                       [7, 9, 4, 1, 3, 5, 8, 6, 2],
                       [5, 8, 1, 9, 7, 4, 3, 2, 6],
                       [4, 7, 6, 2, 1, 3, 5, 9, 8],
                       [2, 3, 9, 5, 8, 6, 7, 1, 4],
                       [9, 5, 7, 4, 6, 2, 1, 8, 3],
                       [1, 2, 3, 8, 5, 7, 6, 4, 9],
                       [6, 4, 8, 3, 9, 1, 2, 5, 7]
                      ])
    removed = remove_moves(full_board)
    assert removed is not None
    assert not is_full(removed)

def test_remove_moves_some_empty():
    partial_board = board.Board([
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ])
    assert not is_full(partial_board)
    removed = remove_moves(partial_board)
    assert removed is not None
    assert not is_full(removed)
    # remove_moves removes some of the numbers, not all

def test_rotate_board():
    input_array = [
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    expected_rotations = [
                            [[1, 2, 4, 0, 0, 0, 0, 0, 0],
                            [5, 0, 0, 9, 7, 0, 0, 1, 0],
                            [0, 3, 0, 0, 0, 8, 2, 0, 0],
                            [0, 0, 5, 2, 9, 7, 3, 0, 0],
                            [6, 0, 3, 5, 0, 4, 1, 0, 9],
                            [0, 0, 8, 3, 1, 6, 5, 0, 0],
                            [0, 0, 2, 7, 0, 0, 0, 3, 0],
                            [0, 6, 0, 0, 2, 3, 0, 0, 5],
                            [0, 0, 0, 0, 0, 0, 9, 4, 2]],

                            [[0, 0, 0, 0, 6, 0, 0, 5, 1],
                            [0, 6, 0, 0, 0, 0, 3, 0, 2],
                            [0, 0, 2, 8, 3, 5, 0, 0, 4],
                            [0, 0, 7, 3, 5, 2, 0, 9, 0], 
                            [0, 2, 0, 1, 0, 9, 0, 7, 0],
                            [0, 3, 0, 6, 4, 7, 8, 0, 0],
                            [9, 0, 0, 5, 1, 3, 2, 0, 0],
                            [4, 0, 3, 0, 0, 0, 0, 1, 0],
                            [2, 5, 0, 0, 9, 0, 0, 0, 0]], 
                            
                            [[2, 4, 9, 0, 0, 0, 0, 0, 0],
                            [5, 0, 0, 3, 2, 0, 0, 6, 0],
                            [0, 3, 0, 0, 0, 7, 2, 0, 0],
                            [0, 0, 5, 6, 1, 3, 8, 0, 0],
                            [9, 0, 1, 4, 0, 5, 3, 0, 6],
                            [0, 0, 3, 7, 9, 2, 5, 0, 0],
                            [0, 0, 2, 8, 0, 0, 0, 3, 0],
                            [0, 1, 0, 0, 7, 9, 0, 0, 5],
                            [0, 0, 0, 0, 0, 0, 4, 2, 1]]
                        ]

    result = rotate_board(input_array)
    assert_equals(result, expected_rotations)
    
def test_generate_puzzle():
    b = generate_puzzle()
    assert b is not None
    assert not is_full(b)