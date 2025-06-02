"""
Importing the Comparator module, since Network builds upon its functionalities:
"""
import comparator2 as Comp
from comparator2 import Comparator

"""
Define a Network as list of Comparators
"""
Network = list[Comparator]

def empty_network() -> Network:
    """
    Return a empty Network
    """
    return []

def append(c: Comparator, net: Network) -> Network:
    """
    Takes a existing Network and appends the new
    Comparator to the end of the list.

    Returns a new Network and does not edit the
    input Network
    """
    copy_net = net[:]
    new_net = copy_net + [c]
    return new_net

def size(net: Network) -> int:
    """
    Counts the size of a Network and return
    the size as a integer
    """
    return len(net)

def max_channel(net: Network) -> int:
    """
    Returns the highest channel where a Network
    will place a value
    """
    return max(list(map(Comp.max_channel,net)))

def is_standard(net: Network) -> bool:
    """
    Checks if a Network only contains standard
    Comparators or not
    """
    return all(list(map(Comp.is_standard,net)))

def apply(net: Network, w: list[int]) -> list[int]:
    """
    applies all the Comparators in a Network
    on a single list of integers

    Returns a new list and does not edit the original
    """
    v = w[:]
    for c in net:
        v = Comp.apply(c,v)
    return v

def outputs(net: Network, w: list[list[int]]) -> list[list[int]]:
    """
    Applies all the Comparators in the Network to
    all lists
    """
    v = w[:] #to avoid side effects

    for i in range(0,len(v)):
        v[i] = apply(net,v[i])

    u = []
    for i in v:
        if i not in u:
            u.append(i)
    return u

def _binary_outputs(n: int) -> list[list[int]]:
    """
    Constructs a list of binary numbers in the
    form of lists of 0's and 1's
    """
    outer = []
    goal = 2**n
    i = 0
    while i < goal:
        inner = []
        m = 0
        j = i
        while n > m:
            if j%2 == 0:
                inner = [0] + inner
            else: #same as i%2 == 1
                inner = [1] + inner
            m = m + 1
            j =  j//2
        i = i + 1
        outer.append(inner)
    return outer

def all_outputs(net: Network, n: int) -> list[list[int]]:
    """
    Returns the binary representation of a Networks
    ability to sort integers
    """
    return outputs(net,_binary_outputs(n))

def is_sorting(net: Network, size: int) -> bool:
    """
    Checks whether a Network is a 
    Sorting Network or not
    """
    outs = all_outputs(net, size)

    if len(outs) < 2:
        return True

    else:
        all_sorted = True
        
        i = 1

        while i < (len(outs) - 1) and all_sorted:
            j = 0

            while j < (len(outs[i]) - 1) and all_sorted:

                if outs[i][j] > outs[i][j+1]:
                    all_sorted = False    
                
                else:
                    j = j + 1
            
            i = i +1
        
        return all_sorted

def to_program(net: Network, var: str, aux: str) -> list[str]:
    """
    Returns a list of commands that applies net to the given list, using the
    given auxiliary variable.

    Recycled Luis' inplementation
    """
    if net == []:
        return []
    else:
        return Comp.to_program(net[-1],var,aux) + to_program(net[:-1],var,aux)