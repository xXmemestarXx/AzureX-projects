"""
In this rewrite we define a Comparator as a tuple of two integers
"""
Comparator = (int,int)

def make_comparator(i: int, j: int) -> Comparator:
    """
    Creates a new Comparator that compares values in
    channel i and j.

    req:
    i != j

    DOCTEST
    >>>print(make_comparator(0,1)
    (0,1)
    """
    return (i,j)

def min_channel(c: Comparator) -> int:
    """
    Returns the channel  where the lowest value
    will be placed
    """
    return c[0]

def max_channel(c: Comparator) -> int:
    """
    Returns the channel where the highest value
    will be placed
    """
    return c[1]

def is_standard(c: Comparator) -> bool:
    """
    Checks whether a comparator is standard or not

    A Comparator is standard when its first value
    is smaller than its second value. In practive it
    means it sorts two values from least to greatest
    """
    return min_channel(c) < max_channel(c)

def apply(c: Comparator, w: list[int]) -> list[int]:
    """
    Sorts the two elements in w according to the values in c

    If the elements are incorrecly placed, return a new list
    where they are sorted. If not return the original list

    req:
    len(w) > min_channel(c)
    len(w) > max_channel(c)
    """
    cmin, cmax = min_channel(c), max_channel(c)

    if w[cmin] > w[cmax]: # not sorted

        copy = w[:] # to avoid side effects

        aux = copy[cmin]

        copy[cmin] = copy[cmax]

        copy[cmax] = aux

        return copy

    else:
        return w

def all_comparators(n: int) -> list[Comparator]:
    """
    Returns all Comparators for n-amount of channels

    Includes non-standard Comparators

    Recycles Luis' inplementation

    req:
    n >= 0
    """
    return [
           make_comparator(i,j)
           for i in range(n)
           for j in range(n)
           if i != j           #i,j need to be different
           ]

def std_comparators(n: int) -> list[Comparator]:
    """
    Returns all standard Comparators for n-amount of channels

    Recycles Luis' inplementation

    req:
    n >= 0
    """
    return [make_comparator(i,j)
            for i in range(n)
            for j in range(i+1,n)]

def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """
    Returns a list of Python commands that descripe how a
    Comparator sorts two values in a list

    Recycles Luis' inplementation

    var and str could be the empty string
    """
    bot = var + "[" + str(min_channel(c)) + "]"
    top = var + "[" + str(max_channel(c)) + "]"
    return ["if " + bot + " > " + top + ":",
            "    " + bot + "," + top + " = " + top + "," + bot]
