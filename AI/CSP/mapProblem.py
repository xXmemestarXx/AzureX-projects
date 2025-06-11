from constraint import *

# Create problem instance
problem = Problem()

# Regions of Australia
regions = ["WA", "NT", "SA", "Q", "NSW", "V"]

# Possible colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Add variables with their domains (possible colors)
problem.addVariables(regions, colors)

# Add constraints so neighboring regions don't have the same color
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []  # Tasmania is not adjacent to any other region
}

# Enforce that neighbors have different colors
for region, adjacent in neighbors.items():
    for neighbor in adjacent:
        problem.addConstraint(lambda a, b: a != b, (region, neighbor))

# Solve the problem
solutions = problem.getSolutions()

# Print first solution
if solutions:
    print(solutions[0])
else:
    print("No solution found.")