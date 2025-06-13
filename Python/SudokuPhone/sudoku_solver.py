import os
import cv2
import numpy as np
import tensorflow as tf
from constraint import Problem, AllDifferentConstraint

import sudoku_utils as sutils

# Global model variable to load once
_loaded_model = None

def load_model():
    global _loaded_model
    if _loaded_model is None:
        model_fpath = "models/model.keras"
        _loaded_model = tf.keras.models.load_model(model_fpath)
    return _loaded_model

def solve_sudoku_with_csp(grid_array):
    problem = Problem()
    rows_chars = "ABCDEFGHI"

    for i in range(9):
        for j in range(9):
            cell = f"{rows_chars[i]}{j+1}"
            val = grid_array[i, j]
            if val == 0:
                problem.addVariable(cell, list(range(1, 10)))
            else:
                problem.addVariable(cell, [int(val)])

    for row_char in rows_chars:
        problem.addConstraint(AllDifferentConstraint(), [f"{row_char}{col}" for col in range(1, 10)])

    for col in range(1, 10):
        problem.addConstraint(AllDifferentConstraint(), [f"{row_char}{col}" for row_char in rows_chars])

    boxes = [
        [f"{r_char}{c_char}" for r_char in rows_grp for c_char in cols_grp]
        for rows_grp in ("ABC", "DEF", "GHI")
        for cols_grp in ("123", "456", "789")
    ]
    for box in boxes:
        problem.addConstraint(AllDifferentConstraint(), box)

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

def solve_image(img_fpath):
    """
    Main callable function to solve sudoku from image path.

    Args:
        img_fpath (str): Path to sudoku image file.

    Returns:
        tuple: (solved_grid (np.array or None), solved_image_path (str or None))
    """
    if not os.path.exists(img_fpath):
        raise FileNotFoundError(f"File not found: '{img_fpath}'")

    # Load and preprocess image
    img = cv2.imread(img_fpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = sutils.resize_and_maintain_aspect_ratio(input_image=img, new_width=1000)

    # Load model once
    model = load_model()

    # Extract cells and board info
    cells, M, board_image = sutils.get_valid_cells_from_image(img)

    # Predict grid digits
    grid_array = sutils.get_predicted_sudoku_grid(model, cells)

    # Solve sudoku using CSP
    solved_board = solve_sudoku_with_csp(grid_array)

    if solved_board is not None and not np.any(solved_board == 0):
        # Generate annotated solution image and save it alongside original
        solved_img = sutils.generate_solution_image(img, board_image, cells, solved_board, M)
        solved_img_path = img_fpath.replace(".jpg", "_solved.jpg").replace(".png", "_solved.png")
        cv2.imwrite(solved_img_path, cv2.cvtColor(solved_img, cv2.COLOR_RGB2BGR))
        return solved_board, solved_img_path
    else:
        # Return None if no full solution found
        return None, None
