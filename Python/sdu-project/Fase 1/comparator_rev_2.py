from dataclasses import dataclass

@dataclass
class Comparator:
    i: int
    j: int

def make_comparator(i: int, j: int) -> Comparator:
    """
    Takes the arguments i and j and returns it as a Comparator datatype
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
    
    If i is the "upper" channel, then the comparator should always sort the input with the lowest being on i
    DOCTEST
    i = 0
    j = 2
    c = make_comparator(i, j)
    >>> is_standard(c)
    True   
    """
    return c.i <= c.j

def apply(c: Comparator, w: list[int]) -> list[int]:
    """
    Uses a comparator on a list of integers.
    This is done by the bubble sort principle
    DOCTEST
    c = make_comparator(i, j)
    w = [3,4,2,5]
    >>> apply(c, w)
    [2,3,4,5]
    """
    for y in range(len(w) - 1): 
        """
        This creates multiple passes through the sorting part in,
        the nested part of the for loop, and ensures we keep sorting until we are done
        """
        for x in range(len(w) - 1):  # For loop to iterate the comparison
            c.i = x
            c.j = x + 1
            
            # Compare the elements at indices c.i and c.j
            if w[c.i] > w[c.j]:  # If the first element is greater, swap them
                w[c.i], w[c.j] = w[c.j], w[c.i]  # Swap elements
    return w

def all_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all possible comparators on n-channels
    """
    # TRY AGAIN BITCH

def std_comparators(n: int) -> list[Comparator]:
    """
    Returns a list with all standard comparators on n-channels.
    """

def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """
    Returns a list of commands that simulates the Comparator.
    """
    instructions = [
        f"Comparator for indices {c.i} and {c.j} using aux variable {aux}, " 
        f"if {var}[{c.i}] > {var}[{c.j}]: "
        f"{aux} = {var}[{c.i}] 'Store {var}[{c.i}] in aux', "
        f"Move {var}[{c.j}] to {var}[{c.i}], {var}[{c.i}] = {var}[{c.j}], "
        f"{var}[{c.j}] = {aux} Move aux ({aux}) (original {var}[{c.i}]) to {var}[{c.j}]"
    ]
    return instructions