from sudoku import sudoku
if __name__ == '__main__':
    sudoku_instance = sudoku()
    sudoku_board = sudoku.board
    sudoku_instance.print_board(sudoku_board)
    sudoku_instance.solve(sudoku_board)
    print("---------------------------------------------")
    sudoku_instance.print_board(sudoku_board)
