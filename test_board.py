from board import Board
from nose.tools import assert_raises
from nose.tools import assert_equals

# Taken from online puzzle generator

def test_is_valid_start_board_valid():
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
    # The Board constructor raises a ValueError if the board is invalid
    # _is_valid_start_board() called by constructor.
    assert Board(input_array)

def test_is_valid_start_board_size_4():
    input_array = [
        [0, 0, 0, 0],
        [1, 2, 3, 4],
        [2, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    assert Board(input_array)

def test_is_valid_start_board_size_25_empty():
    input_array = [[0] * 25 for _ in xrange(25)]
    assert Board(input_array)

def test_is_valid_start_double_digit_values():
    input_array = [[0] * 25 for _ in xrange(25)]
    input_array[0] = range(1, 26)
    assert Board(input_array)

def test_board_constructor_valid():
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
    b = Board(input_array)
    assert_equals(b.board, input_array)

def test_is_valid_start_board_wrong_outer_size():
    input_array = [[1, 0], [0, 0]]
    with assert_raises(ValueError) as cm:
      Board(input_array)
    assert_equals(str(cm.exception), "Board boxes must be square")

def test_is_valid_start_board_wrong_inner_size():
    input_array = [[1, 0], [0, 0], [0, 0],
                   [0, 0], [0, 0], [0, 0],
                   [0, 0], [0, 0], [0, 0]
                  ]
    with assert_raises(ValueError) as cm:
      Board(input_array)
    assert_equals(str(cm.exception), "Board boxes must be square")

def test_is_valid_start_board_not_list():
    input_array = "abcd"
    with assert_raises(TypeError) as cm:
      Board(input_array)
    assert_equals(str(cm.exception), "Board must be a 2D list or tuple")

def test_is_valid_start_board_no_inner_list():
    input_array = ["abcd", "efgh", "i", "j", "k", "l", "m", "n", "o"]
    with assert_raises(TypeError) as cm:
      Board(input_array)
    assert_equals(str(cm.exception), "Board must contain only lists or tuples")

# For now, an empty board is valid
def test_is_valid_start_board_empty():
    b = Board(([[0] * 9 for _ in xrange(9)]))

def test_is_valid_start_board_non_int():
    input_array = [[0] * 9 for _ in xrange(9)]
    input_array[2][2] = "abc"
    with assert_raises(ValueError) as cm:
        Board(input_array)
    assert_equals(str(cm.exception), "Board numbers must be integers " +
                  "in range 0 <= x <= board size")

def test_is_valid_start_board_invalid_ints():
    input_array = [[0] * 9 for _ in xrange(9)]
    input_array[2][2] = 10
    with assert_raises(ValueError) as cm:
        Board(input_array)
    assert_equals(str(cm.exception), "Board numbers must be integers " +
                  "in range 0 <= x <= board size")

def test_is_valid_start_board_duplicates():
    input_array = [
                   # 2 2s in this row
                   [0, 0, 0, 0, 9, 2, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    assert_raises(ValueError, Board, input_array)

def test_is_valid_board_valid():
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
    b = Board(input_array)
    assert b != None

# Duplicates are somewhat hidden in the boxes because I wanted to test
# situations where only the row, column, or box had a duplicate, and
# not multiple situations at the same time.
def test_is_valid_board_duplicate_row():
    input_array = [
                   # 2 2s in this row
                   [0, 0, 0, 0, 9, 2, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    assert_raises(ValueError, Board, input_array)

def test_is_valid_board_duplicate_column():
    input_array = [
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [1, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [1, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   # second 1 in the first column
                   [0, 5, 0, 0, 6, 1, 0, 0, 0]
                  ]
    assert_raises(ValueError, Board, input_array)

def test_is_valid_board_duplicate_in_box():
    input_array = [
                   # second box in first row has two 1s
                   [0, 0, 0, 1, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    assert_raises(ValueError, Board, input_array)

# The _numbers_in_row tests don't need checking for duplicates because
# that will be done when the board is created.
def test_numbers_in_row_valid():
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
    b = Board(input_array)
    result = b._numbers_in_row(0)
    # Two sets are equal iff every element of each set is contained in the other
    assert_equals(result, set((2, 5, 9)))

def test_numbers_in_row_empty():
    input_array = [
                   # Clear out non-zeroes in first row
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_equals(b._numbers_in_row(0), set())

def test_numbers_in_row_invalid_row():
    input_array = [
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_raises(IndexError, b._numbers_in_row, 9)

def test_numbers_in_col_valid():
    input_array = [
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_equals(b._numbers_in_column(8), set((4, 9)))

def test_numbers_in_col_invalid_col():
    input_array = [
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [0, 0, 0, 5, 3, 8, 2, 0, 0],
                   [0, 0, 3, 0, 0, 0, 0, 6, 0],
                   [0, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_raises(IndexError, b._numbers_in_column, "4")

def test_numbers_in_box_valid():
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
    b = Board(input_array)
    assert_equals(b._numbers_in_box(3, 3), set((7, 4, 6, 9, 1, 2, 5, 3)))

def test_numbers_in_box_invalid_params():
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
    b = Board(input_array)
    assert_raises(IndexError, b._numbers_in_box, 1, 1)

def test_valid_moves_valid():
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
    b = Board(input_array)
    result = b.valid_moves(0, 0)
    assert isinstance(result, set)
    assert_equals(result, set((3, 6, 7, 8)))

# Check for a 9 move (no off-by-one error)
def test_valid_moves_9():
    input_array = [
                   [3, 4, 6, 0, 9, 0, 0, 5, 2],
                   [0, 1, 5, 0, 0, 0, 3, 0, 4],
                   [7, 8, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    result = b.valid_moves(1, 0)
    assert_equals(result, set([9]))

# Test a "failed" board where a number has no possible remaining moves
def test_valid_moves_none_left():
    input_array = [
                   # Second number on first row has no moves left
                   [3, 0, 7, 6, 9, 4, 1, 5, 2],
                   [5, 1, 9, 0, 7, 0, 3, 8, 4],
                   [8, 6, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_equals(b.valid_moves(0, 1), set())

def test_valid_moves_position_already_filled():
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
    b = Board(input_array)
    assert_raises(IndexError, b.valid_moves, 1, 1)

def test_valid_moves_invalid_input():
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
    b = Board(input_array)
    assert_raises(IndexError, b.valid_moves, 9, 0)