# Sudoku Solver

This is a Python program that solves a Sudoku puzzle using backtracking and provides a graphical user interface (GUI) for inputting and solving Sudoku boards.

## Features

- Allows users to input their own Sudoku boards through a GUI.
- Validates the inputted Sudoku board for correctness.
- Solves the Sudoku puzzle using a backtracking algorithm.
- Displays the solution on the GUI.

## Requirements

To run the program, you need to have the following installed:

- Python 3.x
- Tkinter library (usually included in Python distributions)

## Usage

1. Ensure that Python and Tkinter are installed on your system.
2. Run the Python script to launch the Sudoku Solver GUI.
3. Enter the numbers of the Sudoku puzzle in the respective cells of the GUI.
4. Press the "Solve" button to solve the Sudoku puzzle.
5. The solved Sudoku puzzle will be displayed in the GUI.
6. To clear the Sudoku board, press the "Clear" button.

## Program Structure

The program consists of two main components: the sudoku class and the GUI implemented using Tkinter.

### The sudoku class

The sudoku class provides methods for creating, validating, and solving Sudoku boards.

#### Methods

- create_new_board(): Fills in the board with a random Sudoku puzzle.
- is_box_valid(board, start_row, start_col): Checks if the 3x3 box starting at the specified position on the board is valid.
- is_sudoku_valid(board): Checks if a Sudoku board is valid.
- create_board(new_board): Creates a Sudoku board by assigning a new board.
- get_board(): Returns the current Sudoku board.
- solve(board): Solves a Sudoku board recursively using backtracking.
- valid(board, num, pos): Checks if a number is valid in a Sudoku board at a given position.
- print_board(board): Prints a Sudoku board.
- find_empty(board): Finds the position of an empty cell in a Sudoku board.

### The GUI

The GUI is implemented using Tkinter, a standard Python library for creating graphical interfaces. It provides a grid of entry widgets for inputting Sudoku boards, as well as buttons for clearing the board and solving the puzzle.

The GUI is structured as follows:

1. The main window contains a title label and a frame for the Sudoku board.
2. The Sudoku board is represented by a grid of entry widgets created using the Entry class from Tkinter.
3. The GUI also includes buttons for clearing the board and solving the puzzle.
4. The GUI is responsive and adjusts the size and position of the elements dynamically.
5. The lines separating the 3x3 boxes are drawn using the Canvas class from Tkinter.

## How it Works

1. The user inputs the numbers of the Sudoku puzzle in the entry widgets.
2. As the user enters numbers, the background color of each entry widget changes to provide visual feedback on the validity of the input.
3. When the user clicks the "Solve" button, the Sudoku board is extracted from the entry widgets.
4. The validity of the inputted Sudoku board is checked using the is_sudoku_valid method of the sudoku class.
5. If the Sudoku board is valid, the solve method of the sudoku class is called to solve the puzzle.
6. The solved Sudoku board is then displayed in the entry widgets, and the background color of the empty cells is changed to indicate the solution.

## Limitations

The program assumes that the Sudoku board is represented by a 9x9 grid of integers, with 0 representing empty cells.
