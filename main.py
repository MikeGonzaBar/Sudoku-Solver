import sudoku

if __name__ == '__main__':
    sudoku_board = (sudoku.sudoku().create_board())
    sudoku.sudoku().print_board(sudoku_board)
    sudoku_board = sudoku.sudoku().solve_board(sudoku_board)
    sudoku.sudoku().print_board(sudoku_board)
