class sudoku:
    def create_board(self):
        # TODO: Fill in the board with a random sudoku puzzle
        return [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

    def print_board(self, board):
        for row in board:
            print(row)
        return

    def solve_board(self, board: list[list[int]]):
      return

    def is_valid_number(self, board: list, row: int, col: int, number: int) -> bool:
        # Check if the number is in the row or column
        for i in range(0, 9):
            if board[row][i] == number:
                return False
            if board[i][col] == number:
                return False

        # Check if the number is in the 3x3 square
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[row_start + i][col_start + j] == number:
                    return False

        return True
