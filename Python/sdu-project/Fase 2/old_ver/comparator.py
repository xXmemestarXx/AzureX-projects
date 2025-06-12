import math
Comparator = int

def make_comparator(i: int, j: int) -> Comparator:
    """Creates a new comparator between the given channels."""
    return (i+j)*(i+j+1)//2+j

def min_channel(c: Comparator) -> int:
    """Returns the channel where the lowest value will be placed
    by c.
    """
    n = math.floor((-1+math.sqrt(1+8*c))/2)
    return n - c + n*(n+1)//2

def max_channel(c: Comparator) -> int:
    """Returns the channel where the highest value will be placed
    by c.
    """
    n = math.floor((-1+math.sqrt(1+8*c))/2)
    return c - n*(n+1)//2

def is_standard(c: Comparator) -> bool:
    """Checks whether the given comparator is standard."""
    return min_channel(c) < max_channel(c)

def apply(c: Comparator, w: list[int]) -> list[int]:
    """
    Sorts the two elements specified by c in w.
    Requires len(w) to be larger than both bottom_channel(c)
    and top_channel(c).
    """
    c_min = min_channel(c);
    c_max = max_channel(c);
    if w[c_min] > w[c_max]:
        v = w[:]
        v[c_min],v[c_max] = w[c_max],w[c_min]
        return v
    else:
        return w

def all_comparators(n: int) -> list[Comparator]:
    """Returns a list of all comparators on n channels."""
    return [make_comparator(i,j)
            for i in range(n)
            for j in range(n)
            if i != j]

def std_comparators(n: int) -> list[Comparator]:
    """Returns a list of all standard comparators on n channels."""
    return [make_comparator(i,j)
            for i in range(n)
            for j in range(i+1,n)]

def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """
    Returns a list of commands that applies c to the given list, using the
    given auxiliary variable.
    """
    bot = var + "[" + str(min_channel(c)) + "]"
    top = var + "[" + str(max_channel(c)) + "]"
    return ["if " + bot + " > " + top + ":",
            "    " + bot + "," + top + " = " + top + "," + bot]
