"""
comparator.py
Made by H8G03: Valdemar, Mathias og Hlynur
"""

from dataclasses import dataclass

"""
Implements a custom dataclass that uses two variables i and j as integers.
This enables creating a instance of a comparator that symbolizes'
the gates of a comparator network.
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
    return Comparator(i, j)

def get_i(c: Comparator):
    """
    Auxillary function to get the i-value of a Comparator
    """
    return(int(c.i))

def get_j(c: Comparator):
    """
    Auxillary function to get the j-value of a Comparator
    """
    return int(c.j)

def get_i_and_j(c: Comparator):
    """
    Auxillary function to get the contents of a Comparator
    as a tuple
    """
    return (int(c.i), int(c.j))
    
def min_channel(c: Comparator) -> int:
    """
    Compares the value of i and j in c and returns the lower value
    
    DOCTEST
    i = 0
    j = 2
    >>> min_channel(Comparator(i, j))
    0
    """
    if(c.i > c.j):
        return c.j
    else:
        return c.i

def max_channel(c: Comparator) -> int:
    """
    Compares the value of i and j in c and returns the higher value
    
    DOCTEST
    i = 0
    j = 2
    >>> max_channel(Comparator(i, j))
    2
    """
    if(c.i < c.j):
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
    return (c.i < c.j) and (c.i != c.j)

def apply(c: Comparator, w: list[int]) -> list[int]:
    """
    Uses a comparator to compare 2 elements in a list of integers and 
    swaps them if needed.
    
    DOCTEST
    c = make_comparator(i, j)
    w = [3,4,2,5]
    >>> apply(c, w)
    [2,3,4,5]
    """

    if(is_standard(c) and w[c.i] > w[c.j]):
        w[c.i], w[c.j] = w[c.j], w[c.i]
    return w

def all_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all possible comparators on n-channels.
    
    DOCTEST
    n = 3
    >>> all_comparators(n)
    [Comparator(i=0, j=1), Comparator(i=0, j=2), Comparator(i=1, j=0),
     Comparator(i=1, j=2), Comparator(i=2, j=0), Comparator(i=2, j=1)]
    """
    comparators=[]
    # This iterates the nested part of the for loop,
    # and ensures we print all combinations of i and j.
    for i in range(n): 
        for j in range(n):
            # Ensures that i and j are not equal, to comply with the defintion of a comparator
            if i != j: 
                comparators.append(Comparator(i,j))
    return comparators

def std_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all standard comparators on n-channels.
    Standard mean that the j-value is always larger than the
    i-value.
    
    DOCTEST
    n = 3
    >>> std_comparators(n)
    [Comparator(i=0, j=1), Comparator(i=0, j=2), Comparator(i=1, j=2)]
    """
    comparators=[]
    # This iterates the nested part of the for loop, 
    # and ensures we print all combinations of i and j.
    for i in range(n): 
        for j in range(n):
            # Checks if i and j are not equal and is a standard comparator
            if(i != j and is_standard(Comparator(i,j))):
                comparators.append(Comparator(i,j))
    return comparators
    
def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """
    Returns a list of instructions that simulates the Comparator.

    DOCTEST
    i = "0"
    j = "1"
    var = "new_list" 
    aux = "temp"
    c = make_comparator(i, j) 
    >>> to_program(c, var, aux)
    ['if new_list[0] > new_list[1]:', 'temp = new_list[0]',
    'new_list[0] = new_list[1]', 'new_list[1] = temp']
    """
    return [
    f"if {var}[{c.i}] > {var}[{c.j}]:",
    f"    {aux} = {var}[{c.i}]",
    f"    {var}[{c.i}] = {var}[{c.j}]",
    f"    {var}[{c.j}] = {aux}"]