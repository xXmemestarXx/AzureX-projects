from constraint import *

problem = Problem()

# Reading user input for Sudoku puzzle - ChatGPT
def read_sudoku_input():
    print("Enter Sudoku puzzle line by line (use 0 or . for blanks):")
    grid = []
    for i in range(9):
        while True:
            line = input(f"Row {i+1}: ").strip()
            if len(line) == 9 and all(c.isdigit() or c == '.' for c in line):
                grid.append([int(c) if c.isdigit() else 0 for c in line])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9) or dots.")
    return grid

sudoku_grid = read_sudoku_input()
rows = "ABCDEFGHI"

# Add variables dynamically based on user input
for i, row_vals in enumerate(sudoku_grid):
    for j, val in enumerate(row_vals):
        cell = f"{rows[i]}{j+1}"
        if val == 0:
            problem.addVariable(cell, list(range(1, 10)))
        else:
            problem.addVariable(cell, [val])

# Add constraints for rows
for row in rows:
    problem.addConstraint(AllDifferentConstraint(), [f"{row}{col}" for col in range(1, 10)])

# Add constraints for columns
for col in range(1, 10):
    problem.addConstraint(AllDifferentConstraint(), [f"{row}{col}" for row in rows])

# Add constraints for boxes
boxes = [
    [f"{r}{c}" for r in rows_grp for c in cols_grp]
    for rows_grp in ("ABC", "DEF", "GHI")
    for cols_grp in ("123", "456", "789")
]
for box in boxes:
    problem.addConstraint(AllDifferentConstraint(), box)

# Formatting the solution for display - ChatGPT
def format_solution(solution):
    if not solution:
        print("No solution found.")
        return
    
    grid = [[0]*9 for _ in range(9)]
    for cell, val in solution.items():
        r = rows.index(cell[0])
        c = int(cell[1]) - 1
        grid[r][c] = val
    
    for i, row in enumerate(grid):
        if i and i % 3 == 0:
            print("+-------+-------+-------+")
        print(" ".join(str(n) if (j + 1) % 3 else f"{n} |" for j, n in enumerate(row)))

solution = problem.getSolution()
if solution:
    print("Solution:")
    format_solution(solution)
else:
    print("No solution found.")