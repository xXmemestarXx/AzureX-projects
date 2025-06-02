class Comparator:
    i:int
    j:int

def make_comparator(i: int, j: int) -> Comparator:
    """
    Takes the arguments i and j and returns it as a Comparator datatype
    """
    return Comparator(i,j)

def min_channel(c: Comparator) -> int:
    """
    Copares the value of i and j in c and returns the lower value
    """
    if(c.i>c.j):
        return c.j
    else:
        return c.i

def max_channel(c: Comparator) -> int:
    """
    Copares the value of i and j in c and returns the higher value
    """
    if(c.i<c.j):
        return c.j
    else:
        return c.i

def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """
    Returns a list of commands that simulates the Comparator.
    """
    return (["if(" + var + "[c.i]>"+ var + "[c.j]):",
                aux + " = " + var + "[c.i]",
                var + "[c.i] = " + var + "[c.j]",
                var + "[c.j] = " + aux])
