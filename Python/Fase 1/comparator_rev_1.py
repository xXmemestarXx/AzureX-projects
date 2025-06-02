from dataclasses import dataclass

@dataclass
class Comparator:
    i: int
    j: int

# Only here because of the need for tests :-D
def make_comparator(i, j) -> Comparator:
    return Comparator(i, j)

def is_standard(c: Comparator) -> bool:
    """
    Checks if c is a standard comparator (it sets the lowest value on the lowest channel)
    
    If i is the "upper" channel, then the comparator should always sort the input with the lowest being on i
    DOCTEST
    i = 2
    j = 0
    c = make_comparator(i, j)
    >>> is_standard(c)
    True
    """
    return c.i >= c.j

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
    comparators = []
    # Use is_standard function, this is fucked no?
    if is_standard:
        return comparators.append(Comparator)
    else: 
        std_comparators(n)

