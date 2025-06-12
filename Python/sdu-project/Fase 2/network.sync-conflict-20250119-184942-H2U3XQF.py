
from comparator2 import Comparator

Network = list[Comparator]
# The comparators are in reverse order, just because.

def empty_network() -> Network:
    """Creates an empty comparator network."""
    return []

def append(c: Comparator, n: Network) -> Network:
    """Adds c to the end of n."""
    return [c] + n

def size(n: Network) -> int:
    """The number of comparators in n."""
    return len(n)

def is_standard(n: Network) -> bool:
    """Checks whether n only contains standard comparators."""
    return all(map(c.is_standard,n))

def apply(n: Network, w: list[int]) -> list[int]:
    """Applies n to w."""
    if n == []:
        return w
    else:
        return(apply(n[:-1],c.apply(n[-1],w)))

def _all_binary_inputs(n: int) -> list[list[int]]:
    """Creates a list with all binary sequences of length n."""
    return [_to_bin(i,n) for i in range(2**n)]

def _to_bin(i: int, n: int) -> list[list[int]]:
    """Converts i to binary in some sense."""
    if n == 0:
        return []
    elif i%2 == 0:
        return [0] + _to_bin(i//2,n-1)
    else:
        return [1] + _to_bin(i//2,n-1)

def outputs(n: Network, w: list[list[int]]) -> list[list[int]]:
    """Applies n to all inputs in w, removing duplicates."""
    if w == []:
        return []
    else:
        next = apply(n, w[0])
        all = outputs(n, w[1:])
        if next in all:
            return all
        else:
            return [next] + all

def all_outputs(net: Network, n: int) -> list[list[int]]:
    """Returns all outputs of a network."""
    return outputs(net,_all_binary_inputs(n))

def _is_sorted(w: list[int]) -> bool:
    """Checks whether w is sorted."""
    return (len(w) < 2 or
            ((w[0] <= w[1]) and _is_sorted(w[1:])))

def is_sorting(net: Network, size: int) -> bool:
    """Checks whether net is a sorting network on size inputs."""
    return all(map(lambda x:_is_sorted(x),
                   all_outputs(net, size)))

def to_program(net: Network, var: str, aux: str) -> list[str]:
    """
    Returns a list of commands that applies net to the given list, using the
    given auxiliary variable.
    """
    if net == []:
        return []
    else:
        return c.to_program(net[-1],var,aux) + to_program(net[:-1],var,aux)
