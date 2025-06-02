"""
filter.py

Written by Hlynur, Mathias and Valdemar H8G03

DM574 Exam project
"""

"""
Importing 3rd party libaries
"""
from dataclasses import *

"""
Importing our lecturer's modules
"""
import network as Netw
import comparator as Comp

@dataclass
class Filter:
    """
    We define a singular Filter as a
    dataclass that contains a network,
    its binary outputs and the amount
    of channels the Filter works on.

    We use a dataclass since it is not
    recommend to use a list containing
    different datatypes
    """
    netw: Netw.Network
    outp: list[list[int]]
    size: int

def make_empty_filter(n: int) -> Filter:
    """
    Preconditions: n > 0

    Returns a filter with an empty network and all binary 
    permutations of length n.

    DOCTEST
    >>> make_empty_filter(2)
    [[], [[0, 0], [1, 0], [0, 1], [1, 1]]]
    """
    net = Netw.empty_network()
    out = Netw._all_binary_inputs(n)
    size = n
    return Filter(net,out,size)

def net(f: Filter) -> Netw.Network:
    """
    Returns the Network of a Filter

    DOCTEST
    test_filter = make_empty_filter(2)
    >>> net(test_filter)
    []
    """
    copy = f.netw
    return copy

def out(f: Filter) -> list[list[int]]:
    """
    Returns the outputs of a Filter

    DOCTEST
    test_filter = make_empty_filter(2)
    >>> out(test_filter)
    [[0, 0], [1, 0], [0, 1], [1, 1]]
    """
    copy = f.outp
    return copy

def size(f: Filter) -> int:
    """
    Returns the size of the filter

    DOCTEST
    test_filter = make_empty_filter(2)
    >>> get_size(test_filter)
    2
    """
    copy = f.size
    return copy

def is_redundant(c: Comp.Comparator, f: Filter)-> bool:
    """
    Checks if the Comparator, c, would be redundant if it were 
    to be added to the Network in the Filter, f.

    DOCTEST
    n = 3
    filt_test = filt.make_empty_filter(n)
    filt_test = filt.add(2, filt_test)
    Filter(n=[2], out=[[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]])
    >>> is_redundant(2, filt_test)
    True
    """
    copy_net = net(f)
    copy_per = out(f)

    copy_net = copy_net + [c]

    new_per = Netw.outputs(copy_net, copy_per)
    return f.outp == new_per

def add(c: Comp.Comparator, f: Filter) -> Filter:
    """
    Appends a Comparator to the end of a Network in
    a Filter

    DOCTEST
    test_comp = Comp.make_comparator(0, 2)
    test_filter = make_empty_filter(3)
    >>> test_filter = add(test_comp, test_filter)
    [[5], [[0, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]]
    """
    new_net = Netw.append(c,net(f))
    new_out = Netw.outputs(new_net, out(f))
    same_size = size(f)
    return Filter(new_net,new_out,same_size)


def is_sorting(f: Filter) -> bool:
    """
    Checks if the network in the filter is a sorting network.

    DOCTEST
    n = 3
    filt_test = filt.make_empty_filter(n)
    filt_test = filt.add(2, filt_test)
    filt_test = filt.add(5, filt_test)
    filt_test = filt.add(8, filt_test)
    Filter(n=[2, 5, 8], out=[[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]], size=3)
    >>> is_sorting(filt_test)
    False
    """
    return (size(f) < 2) or Netw.is_sorting(net(f),size(f))