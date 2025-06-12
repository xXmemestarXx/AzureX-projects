import os
# Suppress TensorFlow logging messages (e.g., GPU warnings, INFO messages)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # This will hide INFO and WARNING messages

import cv2
import numpy as np
import tensorflow as tf
import argparse
from constraint import Problem, AllDifferentConstraint

import sudoku_utils as sutils


def solve_sudoku_with_csp(grid_array):
    """
    Solves a Sudoku puzzle using a Constraint Satisfaction Problem (CSP) approach.

    Args:
        grid_array (np.array): A 9x9 NumPy array representing the Sudoku puzzle.
                                0 indicates a blank cell.

    Returns:
        np.array: A 9x9 NumPy array with the solved Sudoku puzzle, or None if no solution is found.
    """
    problem = Problem()
    rows_chars = "ABCDEFGHI"

    # Add variables dynamically based on the input sudoku_grid
    for i in range(9):
        for j in range(9):
            cell = f"{rows_chars[i]}{j+1}"
            val = grid_array[i, j]
            if val == 0:
                problem.addVariable(cell, list(range(1, 10)))
            else:
                problem.addVariable(cell, [int(val)])

    # Add constraints for rows
    for row_char in rows_chars:
        problem.addConstraint(AllDifferentConstraint(), [f"{row_char}{col}" for col in range(1, 10)])

    # Add constraints for columns
    for col in range(1, 10):
        problem.addConstraint(AllDifferentConstraint(), [f"{row_char}{col}" for row_char in rows_chars])

    # Add constraints for boxes (3x3 subgrids)
    boxes = [
        [f"{r_char}{c_char}" for r_char in rows_grp for c_char in cols_grp]
        for rows_grp in ("ABC", "DEF", "GHI")
        for cols_grp in ("123", "456", "789")
    ]
    for box in boxes:
        problem.addConstraint(AllDifferentConstraint(), box)

    # Get the solution
    solution = problem.getSolution()

    if solution:
        solved_grid = np.zeros((9, 9), dtype=int)
        for cell, val in solution.items():
            r_idx = rows_chars.index(cell[0])
            c_idx = int(cell[1]) - 1
            solved_grid[r_idx, c_idx] = val
        return solved_grid
    else:
        return None


def print_board(board):
    """
    Prints the Sudoku board in a formatted way.

    Args:
        board (np.array): A 9x9 NumPy array representing the Sudoku board.
    """
    if board is None:
        print("No board to print.")
        return

    for i, row in enumerate(board):
        if i and i % 3 == 0:
            print("+-------+-------+-------+")
        print(" ".join(str(n) if (j + 1) % 3 else f"{n} |" for j, n in enumerate(row)))


def solve_sudoku_puzzle(args):
    img_fpath = args['img_fpath']
    # Hardcode the model path directly in the function
    model_fpath = "models/model_15_epochs_font_mnist.keras" 
    
    # Check for valid filepath because cv2.imread fails silently
    if not os.path.exists(img_fpath):
        raise FileNotFoundError (f"File not found: '{img_fpath}'")
    # Load image, change color space from BGR to RGB, and resize
    img = cv2.imread(img_fpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = sutils.resize_and_maintain_aspect_ratio(input_image=img, new_width=1000)

    # Load the trained model and make prediction
    loaded_model = tf.keras.models.load_model(model_fpath)

    # Locate grid cells in image
    cells, M, board_image = sutils.get_valid_cells_from_image(img)

    # Get the 2D array of the puzzle grid to be passed to the solver
    # To hide the progress bar like "2/2 [==============================]",
    # you need to modify the 'sudoku_utils.py' file.
    # Locate the model.predict() call within sutils.get_predicted_sudoku_grid
    # and add 'verbose=0' as an argument, like: model.predict(data, verbose=0)
    grid_array = sutils.get_predicted_sudoku_grid(loaded_model, cells)

    # Print the initial board detected from the image
    print("Detected Sudoku Board (0s are blanks):")
    print_board(grid_array)
    print("\nAttempting to solve...\n")

    # Use the CSP solver function
    solved_board = solve_sudoku_with_csp(grid_array)

    # If a solution is found
    if solved_board is not None:
        # Check if there are no zeros left, meaning it's solved
        if not np.any(solved_board == 0):
            print("Success - sudoku solved!")
            # The annotated image is still generated, but not displayed or saved here
            _ = sutils.generate_solution_image(img, board_image, cells, solved_board, M)
        else:
            print("Solver found a partial solution or could not solve the puzzle completely.")
            print_board(solved_board)
            print("Check for misclassified digits or a very difficult puzzle.\n")
    else:
        print("Could not solve the puzzle. Check for misclassified digits or an unsolvable puzzle.\n")

    # Always print the final state of the board from the solver
    print("Final Sudoku Board:")
    print_board(solved_board if solved_board is not None else grid_array)


if __name__ == "__main__":
    # Construct an argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    # Make img_fpath a required positional argument
    ap.add_argument("img_fpath", type=str, help="Path to sudoku image file")
    # Removed model_fpath from arguments as it's now hardcoded
    args = vars(ap.parse_args())

    solve_sudoku_puzzle(args)
