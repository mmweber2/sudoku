from mock import patch
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
    assert Board._is_valid_start_board(input_array)

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
        Board._is_valid_start_board(input_array)
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

# An empty board is valid, though it doesn't have a unique solution
def test_is_valid_start_board_empty():
    b = Board(([[0] * 9 for _ in xrange(9)]))
    assert b

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
    assert b._is_valid_board()

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
    b = Board(input_array)
    assert not b._is_valid_board()

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
    b = Board(input_array)
    assert not b._is_valid_board()

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
    b = Board(input_array)
    assert not b._is_valid_board()

# The _numbers_in_row tests don't need checking for duplicates because
# that will be done as part of _is_valid_board.
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
    
# Share these between the position functions, since they don't
#   alter the board
pos_check_input_array = [
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
pos_test_board = Board(pos_check_input_array)

def test_numbers_in_row_out_of_range():
    assert_raises(IndexError, pos_test_board._numbers_in_row, 9)

def test_numbers_in_row_non_integer():
    assert_raises(IndexError, pos_test_board._numbers_in_row, "test")

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

def test_numbers_in_col_out_of_range():
    assert_raises(IndexError, pos_test_board._numbers_in_column, 10)

def test_numbers_in_col_non_numeric():
    # Pass a string instead of an int
    assert_raises(IndexError, pos_test_board._numbers_in_column, "4")

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

# Parameters are in the box range, but are not border values
def test_numbers_in_box_in_range_not_border():
    assert_raises(IndexError, pos_test_board._numbers_in_box, 1, 1)

def test_numbers_in_box_non_number_parameters():
    assert_raises(IndexError, pos_test_board._numbers_in_box, "a", "b")

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

def test_string_to_array_full():
    # Broken into substrings for easier visualization
    board_string = ("865729431" + "312648975" + "794135862" + "581974326" +
                    "476213598" + "239586714" + "957462183" + "123857649" +
                    "648391257")
    result = Board.string_to_array(board_string)
    expected = [
                [8, 6, 5, 7, 2, 9, 4, 3, 1],
                [3, 1, 2, 6, 4, 8, 9, 7, 5],
                [7, 9, 4, 1, 3, 5, 8, 6, 2],
                [5, 8, 1, 9, 7, 4, 3, 2, 6],
                [4, 7, 6, 2, 1, 3, 5, 9, 8],
                [2, 3, 9, 5, 8, 6, 7, 1, 4],
                [9, 5, 7, 4, 6, 2, 1, 8, 3],
                [1, 2, 3, 8, 5, 7, 6, 4, 9],
                [6, 4, 8, 3, 9, 1, 2, 5, 7]
                ]
    assert_equals(result, expected)

def test_string_to_array_zeroes():
    board_string = "0" * 81
    result = Board.string_to_array(board_string)
    assert_equals(result, [[0] * 9 for _ in xrange(9)])

def test_string_to_array_partially_full():
    board_string = "040002580080000006007010030000230600300006900800000005000090000600703009700508000"
    result = Board.string_to_array(board_string)
    expected = [[0, 4, 0, 0, 0, 2, 5, 8, 0],
                [0, 8, 0, 0, 0, 0, 0, 0, 6],
                [0, 0, 7, 0, 1, 0, 0, 3, 0],
                [0, 0, 0, 2, 3, 0, 6, 0, 0],
                [3, 0, 0, 0, 0, 6, 9, 0, 0],
                [8, 0, 0, 0, 0, 0, 0, 0, 5],
                [0, 0, 0, 0, 9, 0, 0, 0, 0],
                [6, 0, 0, 7, 0, 3, 0, 0, 9],
                [7, 0, 0, 5, 0, 8, 0, 0, 0]]
    assert_equals(result, expected)

def test_string_to_array_wrong_length():
    board_string = "0" * 80
    assert_raises(ValueError, Board.string_to_array, board_string)

def test_string_to_array_non_ints():
    board_string = "x" * 81
    assert_raises(ValueError, Board.string_to_array, board_string)
