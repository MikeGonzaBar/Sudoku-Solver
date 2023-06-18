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

    def create_board(self, new_board):
        self.board = new_board
        return self.board

    def get_board(self):
        return self.board

    def solve(self, bo):
        if find := self.find_empty(bo):
            row, col = find

        else:
            return True
        for i in range(1, 10):
            if self.valid(bo, i, (row, col)):
                bo[row][col] = i

                if self.solve(bo):
                    return True

                bo[row][col] = 0

        return False

    def valid(self, bo, num, pos):
        # Check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        return not any(
            bo[i][j] == num and (i, j) != pos
            for i, j in itertools.product(
                range(box_y * 3, box_y * 3 + 3), range(box_x * 3, box_x * 3 + 3)
            )
        )

    def print_board(self, bo):
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(bo[i][j])
                else:
                    print(f"{str(bo[i][j])} ", end="")

    def find_empty(self, bo):
        return next(
            (
                (i, j)
                for i, j in itertools.product(range(len(bo)), range(len(bo[0])))
                if bo[i][j] == 0
            ),
            None,
        )
