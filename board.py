from math import sqrt

class Board(object):
    """Represents a Sudoku board."""

    def __init__(self, board_array):
        """Creates a new Sudoku puzzle board.

        Per the rules of Sudoku, each board consists of 9 squares, each
        of which contains 9 numbers in a 3x3 box. Each number appears
        exactly once in each 3x3 square, row, and column.
        Does not test whether board_array has duplicate values.

        Args:
            board_array: A 9x9 2D list containing the initial board setup.
            Blank spaces are represented by zeroes, and filled spaces are
            represented by integers 1-9.

        Raises:
            ValueError: board_array is not a valid board configuration.
        """
        if not Board._is_valid_start_board(board_array):
            raise ValueError("Invalid start board configuration.")
        self.board = board_array
        self.board_size = len(board_array)
        self.box_size = int(sqrt(self.board_size))

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.board)

    # TODO: Check if this board has multiple solutions
    @staticmethod
    def _is_valid_start_board(board_array):
        """Confirms that a board array is in valid Sudoku format.

        Does not confirm whether it is possible to solve this board.
        Does not confirm whether this board has duplicate values.

        Returns:
            True if board_array is in the valid format.

        Raises:
            TypeError: board_array is not a list or tuple.

            ValueError: board_array is not a valid board configuration.
        """
        if type(board_array) not in (list, tuple):
            raise TypeError("Board must be a 2D list or tuple")
        board_size = len(board_array)
        box_size = int(board_size**0.5)
        # box_size converts to an int, so make sure it's really a square number
        if box_size * box_size != board_size:
            raise ValueError("Board boxes must be square")
        valid_values = set(xrange(board_size + 1))
        for sublist in board_array:
            if type(sublist) not in (list, tuple):
                raise TypeError("Board must contain only lists or tuples")
            if len(sublist) != board_size:
                raise ValueError("Board boxes must be square")
            for item in sublist:
                if item not in valid_values:
                    raise ValueError(
                        "Board numbers must be integers in range " +
                        "0 <= x <= board size")
        return True

    def _is_valid_board(self):
        """Determines whether this Board is valid.

        A Board is considered valid if there are no repeating numbers
        (besides 0, which represents a blank space) in any row, column,
        or box of the board. Boxes must be square, and are 3 x 3 on
        a standard board.
        For a standard board, the 3 x 3 boxes divide the board into ninths
        such that exactly 9 fit onto the board. For example, there can be
        repeating numbers in the 3 columns that span indices 1-3, but not
        0-2, because 0-2 and 3-5 are separate boxes.

        Returns:
            True iff the board is valid, and False otherwise.
        """
        # We can't use _numbers_in_row, _numbers_in_column,
        #    or _numbers_in_box for these because those don't
        #    check for duplicates.
        # Check rows
        for i in xrange(self.board_size):
            row_numbers = set()
            for number in self.board[i]:
                if number == 0:
                    continue
                if number in row_numbers:
                    return False
                row_numbers.add(number)
        # Check columns
        for j in xrange(self.board_size):
            col_numbers = set()
            for i in xrange(self.board_size):
                number = self.board[i][j]
                if number == 0:
                    continue
                if number in col_numbers:
                    return False
                col_numbers.add(number)
        # Check boxes
        # Start at upper left of each box, then move one box width in each direction
        move_range = xrange(0, self.board_size, self.box_size)
        boxes = [(x, y) for x in move_range for y in move_range]
        for box_x, box_y in boxes:
            box_numbers = set()
            for i in xrange(box_x, box_x + self.box_size):
                for j in xrange(box_y, box_y + self.box_size):
                    number = self.board[i][j]
                    if number == 0:
                        continue
                    if number in box_numbers:
                        return False
                    box_numbers.add(number)
        return True

    def _numbers_in_row(self, row):
        """Returns a set of the numbers in this row.

        Zeroes are ignored, since they represent blank spaces.

        Args:
            row: The zero-indexed integer of the row of this board to check.
            Must be in the range 0 <= x < board_size, so 0 <= x < 9
            for a standard 9x9 board.

        Returns:
            A set of the non-zero numbers found in this row.

        Raises:
            IndexError: row is outside the valid range for this board.
        """
        if not self._valid_pos(row):
            raise IndexError("Row {} is not a valid integer".format(row))
        return set(self.board[row]) - set([0])

    def _numbers_in_column(self, col):
        """Returns a set of the numbers in this column.

        Zeroes are ignored, since they represent blank spaces.

        Args:
            col: The zero-indexed integer of the column of this board to check.
            Must be in the range 0 <= x < board_size, so 0 <= x < 9
            for a standard 9x9 board.

        Returns:
            A set of the non-zero numbers found in this column.

        Raises:
            IndexError: col is outside the valid range for this board.
        """
        if not self._valid_pos(col):
            raise IndexError("Column {} is not a valid integer".format(col))
        col_numbers = set()
        for i in xrange(self.board_size):
            if self.board[i][col] != 0:
                col_numbers.add(self.board[i][col])
        return col_numbers

    def _numbers_in_box(self, box_start_row, box_start_col):
        """Returns a set of the numbers in the given box.

        Zeroes are ignored, since they represent blank spaces.

        For example, to check the first box, box_start_row and
        box_start_col should be 0 and 0. To check the center box,
        they should be 3 and 3.

        For a standard 9x9 board, the only acceptable values for box_start_row
        and box_start_col are 0, 3, and 6.

        Args:
            box_start_row: The row index of the upper left most number in the
              box.

            box_start_col: The column index of the upper left most number in
              the box.

        Returns:
            A set of the non-zero numbers found in this box.

        Raises:
            TypeError: box start values are not integers.

            IndexError: box start values are outside the valid range
               for this board.
        """
        # Don't use _valid_pos; box requirements are more specific
        size = self.board_size
        for start in (box_start_row, box_start_col):
            if not isinstance(start, int):
                raise TypeError("Box start numbers must be integers")
            if not (0 <= start < size and start % self.box_size == 0):
                raise IndexError("Invalid box start number: {}".format(start))
        box_numbers = set()
        for i in xrange(box_start_row, box_start_row + self.box_size):
            for j in xrange(box_start_col, box_start_col + self.box_size):
                if self.board[i][j] != 0:
                    box_numbers.add(self.board[i][j])
        return box_numbers

    def valid_moves(self, row, column):
        """Returns the valid moves for the given position.

        Args:
            row, column: The zero-indexed integer row and column
            numbers for the position to check. Must be in the range
            0 <= x < board_size.

        Returns:
            A set of numbers in the range 1 to board size (inclusive)
            that are not already part of the given position's row,
            column, or box, and so can be played at the given position.

        Raises:
            IndexError: The position at row, column is not empty; it
            contains a number > 0.
        """
        if not (self._valid_pos(row) and self._valid_pos(column)):
            raise IndexError("Invalid row or column index.")
        if self.board[row][column] != 0:
            raise IndexError(
                "Non-zero number already at position {},{}: {}".format(
                    row, column, self.board[row][column])
                )
        print "Board is currently "
        print self
        print "Row, col are ", row, column
        used_numbers = self._numbers_in_row(row)
        # Combine all the used numbers together because we don't care where
        # they were used, just that they are no longer possible
        used_numbers.update(self._numbers_in_column(column))
        # Round row and column numbers down to box start positions
        x = row / self.box_size * self.box_size
        y = column / self.box_size * self.box_size
        used_numbers.update(self._numbers_in_box(x, y))
        print "Used numbers is now ", used_numbers
        return set(xrange(1, self.board_size + 1)) - used_numbers

    def _valid_pos(self, index):
        """Checks whether the given index is valid for this Board.

        Args:
            index: integer, the index to check. A valid index is an integer in
            the range 0 <= x < board_size.

            Since all Boards must be square, a valid row number is a
            valid column number, and vice versa.

        Returns:
            True iff index is a valid row or column index.
        """
        return index in xrange(self.board_size)

    def make_move(self, row, column, play):
        """If possible, plays the given number at the given position.

        Does not check whether the move is the right answer for that position.
        Does not check the validity of the indices or the play.

        A play of 0 is considered undoing a move.

        Args:
            row, column: The zero-indexed integer row and column
                numbers for the position. Must be in the range
                0 <= x < board_size.
            play: The number to play at this position. Must be in the range
                0 <= x < board_size.
        """
        self.board[row][column] = play