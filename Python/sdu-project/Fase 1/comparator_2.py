from dataclasses import dataclass
#from network.py import *
@dataclass
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

def all_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all comparators
    """
    comparators=[]
    for i in range(n):
        for j in range(n):
            comparators.append(Comparator(i,j))
    return (comparators)

def std_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all standard comparators
    """
    comparators=[]
    for i in range(n):
        for j in range(n):
            if( i!=j and is_standard(Comparator(i,j))):
                comparators.append(Comparator(i,j))
    return (comparators)

def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """
    Returns a list of commands that simulates the Comparator.
    """
    i=string(c.i)
    j=string(c.j)
    #code nr 1
"""
    if(c.i>c.j):
        return["Sammenligner indeks" + i + " og " + j,
            " byt indeks" + i + " og " + j]
    else:
        return ["Sammenligner indeks" + i + " og " + j,
        " bytter dem ikke"]
    """
    # code nr 2
    """
    return (["if(" + var + "[c.i]>"+ var + "[c.j]):",
                aux + " = " + var + "[c.i]",
                var + "[c.i] = " + var + "[c.j]",
                var + "[c.j] = " + aux])
"""
