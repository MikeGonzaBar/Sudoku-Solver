import itertools


class sudoku:

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def create_new_board(self):
        # TODO: Fill in the board with a random sudoku puzzle
        pass

    def is_box_valid(self, board, start_row, start_col):
        seen = set()

        for row, col in itertools.product(range(start_row, start_row + 3), range(start_col, start_col + 3)):
            cell_value = board[row][col]

            if cell_value != 0:
                if cell_value in seen:
                    return False
                seen.add(cell_value)

        return True

    def is_sudoku_valid(self, board):
        for row, col in itertools.product(range(0, 9, 3), range(0, 9, 3)):
            if not self.is_box_valid(board, row, col):
                return False

        # Check rows
        for row in range(9):
            seen = set()
            for col in range(9):
                cell_value = board[row][col]
                if cell_value != 0:
                    if cell_value in seen:
                        return False
                    seen.add(cell_value)

        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                cell_value = board[row][col]
                if cell_value != 0:
                    if cell_value in seen:
                        return False
                    seen.add(cell_value)

        return True

    def create_board(self, new_board):
        self.board = new_board
        return self.board

    def get_board(self):
        return self.board

    def solve(self, board):
        if find := self.find_empty(board):
            row, col = find

        else:
            return True
        for i in range(1, 10):
            if self.valid(board, i, (row, col)):
                board[row][col] = i

                if self.solve(board):
                    return True

                board[row][col] = 0

        return False

    def valid(self, board, num, pos):
        # Check row
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        return not any(
            board[i][j] == num and (i, j) != pos
            for i, j in itertools.product(
                range(box_y * 3, box_y * 3 + 3), range(box_x * 3, box_x * 3 + 3)
            )
        )

    def print_board(self, board):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(board[i][j])
                else:
                    print(f"{str(board[i][j])} ", end="")

    def find_empty(self, board):
        return next(
            (
                (i, j)
                for i, j in itertools.product(range(len(board)), range(len(board[0])))
                if board[i][j] == 0
            ),
            None,
        )
