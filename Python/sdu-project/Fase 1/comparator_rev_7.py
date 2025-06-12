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
    return (int(c.i),int(c.j))
    

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

    print(f"w[c.i] is: {w[c.i]}")
    print(f"w[c.j] is: {w[c.j]}")
    print("")

    # Note: This function has O(n^2) runtime
    if(is_standard(c) and w[c.i] > w[c.j]):
        w[c.i], w[c.j] = w[c.j], w[c.i]
    return w

def all_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all comparators on n-channels.
    
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
    Returns a list of all standard comparators on n-channels.
    Standard mean that the j-value is always larger than the
    i-value
    
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

# def to_program(c: Comparator, var: str, aux: str) -> list[str]:
#     """
#     Returns Python code in a list of str, where each index is a line shift.
#     The code simulates the primary function of a Comparator, aka 
#     sorting the order of two values. Very similar to apply()

#     var is a str of a list that reprents the values that need to be sorted.
#     For example '[2,1]' and '[9,7]' are elligible inputs.

#     aux is a empty value whose purpose is to temporarily hold
#     the contents of a index of var. This is neccesary because
#     the code need to switch the values of two indexes.
#     It is meant to be overwritten in the output Python code.
    
#     DOCTEST
#     i = "i"
#     j = "j"
#     var = "network", 
#     aux = "temp"
#     c = make_comparator(i, j) 
#     >>> to_program(c, var, aux)
#     ["Comparator for indices i and j using the aux variable as temp, and the list 'network'.
#     if network[i] > network[j]: 
#         'Store network[i] in aux (temp)' temp = network[i],
#         'Move network[j] to network[i]' network[i] = network[j],
#         'Insert temp on index j' network[j] = temp
#     """
#     code = [
#         f"if {var}[{c.i}] > {var}[{c.j}]:",
#         f"  {aux} = {var}[{c.i}]",
#         f"  {var}[{c.i}] = {var}[{c.j}]",
#         f"  {var}[{c.j}] = {aux}"
#     ]

#     return code