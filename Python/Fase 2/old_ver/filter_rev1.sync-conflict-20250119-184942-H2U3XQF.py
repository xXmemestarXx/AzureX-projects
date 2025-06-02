import network as Netw
import comparator as Comp
from dataclasses import *

Filter = list[Netw.Network, list[list[int]]]

def make_empty_filter(n: int) -> Filter:
    """
    Returns a filter with an empty network and all binary permutations of length n.

    DOCTEST
    >>> make_empty_filter(2)
    [[], [[0, 0], [1, 0], [0, 1], [1, 1]]]
    """
    net = Netw.empty_network()
    out = Netw._all_binary_inputs(n)
    return[net, out]

def net(f: Filter) -> Netw.Network:
    """
    Returns the network of a filter

    DOCTEST
    test_filter = make_empty_filter(2)
    >>> net(test_filter)
    []
    """
    copy = f[:]
    return copy[0]

def out(f: Filter) -> list[list[int]]:
    """
    Returns the outputs of a filter

    DOCTEST
    test_filter = make_empty_filter(2)
    >>> out(test_filter)
    [[0, 0], [1, 0], [0, 1], [1, 1]]
    """
    copy = f[:]
    return copy[1]

def is_redundant(c: Comp.Comparator, f: Filter)-> bool:
    """
    Checks if the comparator is redundant by adding it to the network
    and seeing if it changes the output of any of the binary lists from
    all_outputs() in network.py.

    DOCTEST
    test_comp = make_comparator(0, 2)
    test_filter = make_empty_filter(2)
    """

    copy_net = net(f)
    copy_per = out(f)

    copy_net = copy_net + [c]

    new_per = Netw.outputs(copy_net, copy_per)
    return f[1] == new_per

def add(c: Comp.Comparator, f: Filter) -> Filter:
    """
    Appends a comparator to the end of a network

    DOCTEST
    test_comp = Comp.make_comparator(0, 2)
    test_filter = make_empty_filter(3)
    >>> test_filter = add(test_comp, test_filter)
    [[5], [[0, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]]
    """
    new_net = list(net(f)) + [c]
    new_out = Netw.outputs(new_net, out(f))
    return [new_net, new_out] 


def is_sorting(f: Filter) -> bool:
    """
    Checks if the network in the filter is a sorting network.

    DOCTEST
    
    """
    return (len(out(f)[0]) < 2) or Netw.is_sorting(net(f),len(out(f)))