import itertools
import tkinter as tk
from tkinter import messagebox

from sudoku import sudoku


def clear_sudoku() -> None:
    """
    Clear the Sudoku board by removing all the entries and resetting their background color.

    Returns:
        None
    """
    for row in entries:
        for entry in row:
            entry.delete(0, tk.END)
            entry.config(bg="white")
    return


def solve_sudoku() -> None:
    """
    Solve the Sudoku puzzle based on the current entries.

    Returns:
        None
    """
    try:
        board = get_entries()
    except Exception:
        messagebox.showerror("Error", "Invalid input")
        return
    sudoku_instance.create_board(board)
    if not sudoku_instance.is_sudoku_valid(board):
        messagebox.showerror("Error", "Invalid sudoku")
        return
    sudoku_instance.solve(board)
    upload_entries(board)
    return


def on_entry_change(event) -> None:
    """
    Handle the event triggered when the content of an entry widget is changed.

    Args:
        event: The event object associated with the entry widget.

    Returns:
        None
    """
    entry = event.widget
    input_text = entry.get()

    if input_text.isdigit():
        entry.config(bg="light grey")
    elif input_text == "":
        entry.config(bg="white")
    else:
        entry.config(bg="red")


def get_entries() -> list[list[int]]:
    """
    Get the current entries from the Sudoku board.

    Returns:
        list[list[int]]: A 9x9 Sudoku board represented as a 2-dimensional list of integers.
            Each integer represents the value in the corresponding cell on the board.
    """
    result = []
    for row in entries:
        sublist = []
        for entry in row:
            if text := entry.get():
                sublist.append(int(text))
            else:
                sublist.append(0)
        result.append(sublist)
    return result


def upload_entries(solution) -> None:
    """
    Upload the solution to the Sudoku board entries.

    Args:
        solution (list[list[int]]): A 9x9 Sudoku solution represented as a 2-dimensional list of integers.
            Each integer represents the value in the corresponding cell on the board.

    Returns:
        None
    """
    for i, j in itertools.product(range(9), range(9)):
        if entries[i][j].get() == '':
            entries[i][j].config(bg="light blue")
        entries[i][j].delete(0, tk.END)
        entries[i][j].insert(0, str(solution[i][j]))
    return


def draw_lines() -> None:
    """
    Draw the lines on the Sudoku board.

    Returns:
        None
    """
    canvas.delete("lines")
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    for i in range(1, 3):
        y = i * height / 3
        canvas.create_line(0, y, width, y, width=2, tags="lines")

    for j in range(1, 3):
        x = j * width / 3
        canvas.create_line(x, 0, x, height, width=2, tags="lines")
    return


# Create the main window
sudoku_instance = sudoku()
window = tk.Tk()
window.title("Sudoku Solver")
window.configure(bg="white")

# Create a title label
title_label = tk.Label(window, text="Sudoku Solver", activebackground="white", bg="white", fg="black",
                       font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Create a frame for the table
frame = tk.Frame(window)
frame.pack(fill="both", expand=True)
# Create a canvas on top of the grid
canvas = tk.Canvas(frame, width=1, height=1,
                   bg="white", highlightthickness=0)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

# Call draw_lines initially
draw_lines()

# Bind draw_lines to <Configure> event
canvas.bind("<Configure>", lambda e: draw_lines())
# Create a 2D list to hold the text entry widgets
entries = []
for i in range(9):
    row = []
    for j in range(9):
        entry = tk.Entry(frame, width=5, background="white",
                         fg="black", font=("Arial", 12))
        # Bind the on_entry_change function to the <KeyRelease> event
        entry.bind("<KeyRelease>", on_entry_change)
        entry.grid(row=i, column=j, padx=3, pady=3, sticky="nsew")
        row.append(entry)
    entries.append(row)

# Create a frame for the buttons
button_frame = tk.Frame(window, bg="white")
button_frame.pack()

# Create the buttons
button1 = tk.Button(button_frame, text="Clear",
                    command=clear_sudoku, font=("Arial", 11), background="white")
button1.grid(row=0, column=0, padx=5, pady=10)

button2 = tk.Button(button_frame, text="Solve",
                    command=solve_sudoku, font=("Arial", 11), background="white")
button2.grid(row=0, column=1, padx=5, pady=10)

# Configure row and column weights
for i in range(9):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

# Start the main event loop
window.mainloop()
