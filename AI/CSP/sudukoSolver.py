from constraint import *

problem = Problem()

""" Blank board
problem.addVariables(
    [
        "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9",
        "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9",
        "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9",
        "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9",
        "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9",
        "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9",
        "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9",
        "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9",
        "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9"
    ],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
"""

problem.addVariables(
    [
        "A1", "A2", "A4", "A6", "A8", "A9",
        "B2", "B3", "B5", "B7", "B8",
        "C1", "C2", "C5", "C8", "C9",
        "D1", "D2", "D5", "D8", "D9",
        "E1", "E2", "E3", "E4", "E5", "E6", "E8",
        "F1", "F2", "F5", "F8", "F9",
        "G1", "G2", "G5", "G8", "G9",
        "H2", "H3", "H5", "H7", "H8",
        "I1", "I2", "I4", "I6", "I8", "I9"
    ],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
#%% Defining assigned fields
problem.addVariable("A3", [3])
problem.addVariable("A5", [2])
problem.addVariable("A7", [6])
problem.addVariable("B1", [9])
problem.addVariable("B4", [3])
problem.addVariable("B6", [5])
problem.addVariable("B9", [1])
problem.addVariable("C3", [1])
problem.addVariable("C4", [8])
problem.addVariable("C6", [6])
problem.addVariable("C7", [4])
problem.addVariable("D3", [8])
problem.addVariable("D4", [1])
problem.addVariable("D6", [2])
problem.addVariable("D7", [9])
problem.addVariable("E7", [7])
problem.addVariable("E9", [8])
problem.addVariable("F3", [6])
problem.addVariable("F4", [7])
problem.addVariable("F6", [8])
problem.addVariable("F7", [2])
problem.addVariable("G3", [2])
problem.addVariable("G4", [6])
problem.addVariable("G6", [9])
problem.addVariable("G7", [5])
problem.addVariable("H1", [8])
problem.addVariable("H4", [2])
problem.addVariable("H6", [3])
problem.addVariable("H9", [9])
problem.addVariable("I3", [5])
problem.addVariable("I5", [1])
problem.addVariable("I7", [3])
#%%

# Adding constraint for variables being different in rows
for row in "ABCDEFGHI":
    problem.addConstraint(AllDifferentConstraint(), [f"{row}{col}" for col in range(1, 10)])

# Adding constraint for variables being different in columns
for col in range(1, 10):
    problem.addConstraint(AllDifferentConstraint(), [f"{row}{col}" for row in "ABCDEFGHI"])

# Adding constraint for variables being different in 3x3 box
boxes = [
    [f"{r}{c}" for r in rows for c in cols]
    for rows in ("ABC", "DEF", "GHI")
    for cols in ("123", "456", "789")
]

for box in boxes:
    problem.addConstraint(AllDifferentConstraint(), box)

# Formatting the solution - ChatGPT
def format_solution(solution):
    if not solution:
        print("No solution found.")
        return
    
    grid = [[0 for _ in range(9)] for _ in range(9)]
    rows = "ABCDEFGHI"
    
    for cell, value in solution.items():
        row = rows.index(cell[0])
        col = int(cell[1]) - 1
        grid[row][col] = value
    
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("+-------+-------+-------+")
        print(" ".join(str(n) if (j + 1) % 3 != 0 else f"{n} |" for j, n in enumerate(row)))

# Get and display solutions
solutions = problem.getSolutions()

if solutions:
    print("Solution:")
    format_solution(solutions[0])
else:
    print("No solutions found.")

