from dataclasses import dataclass

"""
Implements a custom dataclass that uses two variables i and j as integers.
This enables creating a instance of comparator that symbolizes the gates of a comparatornetwork.
"""
@dataclass
class Comparator:
    i: int
    j: int

def make_comparator(i: int, j: int) -> Comparator:
    """
    Takes the arguments i and j and returns a Comparator instance with the arguments.
    DOCTEST
    i = 0
    j = 2
    >>> make_comparator(i, j)
    Comparator(0, 2)
    """
    return Comparator(i,j)

def min_channel(c: Comparator) -> int:
    """
    Compares the value of i and j in c and returns the lower value
    DOCTEST
    i = 0
    j = 2
    >>> min_channel(Comparator(i, j))
    0
    i = 2
    j = 0
    >>> min_channel(Comparator(i, j))
    0
    """
    if(c.i>c.j):
        return c.j
    else:
        return c.i

def max_channel(c: Comparator) -> int:
    """
    Compares the value of i and j in c and returns the higher value
    DOCTEST
    i = 0
    j = 2
    >>> min_channel(Comparator(i, j))
    2
    i = 2
    j = 0
    >>> min_channel(Comparator(i, j))
    2
    """
    if(c.i<c.j):
        return c.j
    else:
        return c.i

def is_standard(c: Comparator) -> bool:
    """
    Checks if c is a standard comparator (it sets the lowest value on the lowest channel)
    DOCTEST
    i = 0
    j = 2
    c = make_comparator(i, j)
    >>> is_standard(c)
    True   
    """
    return c.i <= c.j and c.i != c.j

def apply(c: Comparator, w: list[int]) -> list[int]:
    """
    Uses a comparator on a list of integers.
    DOCTEST
    c = make_comparator(i, j)
    w = [3,4,2,5]
    >>> apply(c, w)
    [2,3,4,5]
    """
    """
    This iterates the nested part of the for loop, and ensures we keep sorting until we are done.
    """
    for y in range(len(w) - 1): 
        """
        For loop for sorting the list of integers with the use of a comparator.
        """
        for x in range(len(w) - 1):
            c.i = x
            c.j = x + 1
            """
            Compare the elements at indices c.i and c.j, if the i element is greater, swap them
            """
            if w[c.i] > w[c.j]:
                w[c.i], w[c.j] = w[c.j], w[c.i]  # Swap elements by assigning to the opposite variable
    return w

def all_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all comparators on n-channels
    DOCTEST
    n = 3
    >>> all_comparators(n)
    [Comparator(i=0, j=1), Comparator(i=0, j=2), Comparator(i=1, j=0), Comparator(i=1, j=2), Comparator(i=2, j=0), Comparator(i=2, j=1)]
    """
    comparators=[]
    """
    This iterates the nested part of the for loop, and ensures we print all combinations of i and j.
    """
    for i in range(n):
        for j in range(n):
            if i != j: # Ensures that i and j are not equal, to comply with the defintion of a comparator
                comparators.append(Comparator(i,j))
    return comparators

def std_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all standard comparators on n-channels
    DOCTEST
    n = 3
    >>> std_comparators(n)
    [Comparator(i=0, j=1), Comparator(i=0, j=2), Comparator(i=1, j=2)]
    """
    comparators=[]
    """
    This iterates the nested part of the for loop, and ensures we print all combinations of i and j.
    """
    for i in range(n):
        for j in range(n):
            if(i != j and is_standard(Comparator(i,j))): # Checks if i and j are not equal and is a standard comparator
                comparators.append(Comparator(i,j))
    return comparators

def to_program(c: Comparator, var: str, aux: str) -> str:
    """
    Returns a list of instructions that simulates the Comparator.
    DOCTEST
    i = "i"
    j = "j"
    var = "network", 
    aux = "temp"
    c = make_comparator(i, j) 
    >>> to_program(c, var, aux)
    Comparator for indices i and j using aux variable temp, and list network.
    if network[i] > network[j]:
        'Store network[i] in aux (temp)' temp = network[i],
        'Move network[j] to network[i]', network[i] = network[j],
        'Insert temp on index j' network[j] = temp
    if network[j] > network[i]:
        'Store network[j] in aux (temp)' temp = network[j],
        'Move network[i] to network[j]', network[j] = network[i],
        'Insert temp on index i' network[i] = temp
    """
    """
    Creates a multi-line f-string that uses the given arguments to craft a list of instructions and returns them.
    """
    instructions = (f"Comparator for indices i and j using the aux variable as {aux}, and the list '{var}'.\n"
    f"if {var}[{c.i}] > {var}[{c.j}]:\n"
    f"    'Store {var}[{c.i}] in aux ({aux})' {aux} = {var}[{c.i}],\n"
    f"    'Move {var}[{c.j}] to {var}[{c.i}]' {var}[{c.i}] = {var}[{c.j}],\n"
    f"    'Insert temp on index j' {var}[{c.j}] = {aux}\n"
    f"if {var}[{c.j}] > {var}[{c.i}]:\n"
    f"    'Store {var}[{c.j}] in aux ({aux})' {aux} = {var}[{c.j}],\n"
    f"    'Move {var}[{c.i}] to {var}[{c.j}]' {var}[{c.j}] = {var}[{c.i}],\n"
    f"    'Insert temp on index i' {var}[{c.i}] = {aux}")

    return instructions