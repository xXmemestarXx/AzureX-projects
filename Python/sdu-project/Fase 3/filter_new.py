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
    Returns a filter with an empty network and all binary permutations of length n.
    """
    netw = Netw.empty_network()
    outp = Netw.all_outputs(netw,n)
    size = n
    return Filter(netw,outp,size)

def net(f: Filter) -> Netw.Network:
    """
    Returns the Network of a input Filter
    """
    return f.netw

def out(f: Filter) -> list[list[int]]:
    """
    Returns the outputs of a Filter
    """
    return f.outp

def size(f: Filter) -> int:
    """
    Returns the size of the filter
    """
    return f.size

def is_redundant(c: Comp.Comparator, f: Filter)-> bool:
    """
    Checks if the Comparator, c, would be redundant if it were 
    to be added to the Network in the Filter, f.

    Note: 
    Copies of the same Comparator repeated after each other
    are always redundant.

    DOCTEST
    n = 3
    Filter = make_empty_filter(3)
    Comparator = Comp.make_comparator(0,1)
    Bigger_Filter = add(Comparator,Filter)

    >>> is_redundant(Comparator,Filter)
    false
    
    >>> is_redundant(Comparator,Bigger_Filter)
    True
    """
    new_filter = add(c,f)
    return out(new_filter) == out(f)

# def add(c: Comp.Comparator, f: Filter) -> Filter:
#     """
#     Appends a Comparator to the end of a Network in
#     a Filter

#     The slow version that is paired with the fast version of is_sorting()

#     DOCTEST:
#     n = 3
#     Comparator = Comp.make_comparator(0, 2)
#     Filter = make_empty_filter(n)

#     >>> Bigger_Filter = add(Comparator, Filter)

#     >>> print(out(BiggerFilter))
#     Network[Comparator]
#     """
#     new_net = Netw.append(c,net(f))
#     new_out = Netw.outputs(new_net, out(f))
#     same_size = size(f)
    
#     return Filter(new_net,new_out,same_size)

def add(c: Comp.Comparator, f: Filter) -> Filter:
    """
    Appends a Comparator to the end of a Network in
    a Filter

    The fast version that is paired with the slow version of is_sorting()

    DOCTEST:
    n = 3
    Comparator = Comp.make_comparator(0, 2)
    Filter = make_empty_filter(n)

    >>> Bigger_Filter = add(Comparator, Filter)

    >>> print(out(BiggerFilter))
    Network[Comparator]
    """
    new_net = Netw.append(c,net(f))
    
    new_out = Netw.outputs(Netw.append(c,Netw.empty_network()), out(f)) #if duplicates in the outputs needs to be removed
    # new_out = [Comp.apply(c, x) for x in out(f)]                      #if not
    
    same_size = size(f)
    
    return Filter(new_net,new_out,same_size)



# def is_sorting(f: Filter) -> bool:
#     """
#     Checks if the network in the filter is a sorting network.

#     The fast version that is paired with the slow version of add()

#     DOCTEST
#     n = 3
    
#     Small_Filter = make_empty_filter(n)
    
#     fir = Comp.make_comparator(0,1)
#     sec = Comp.make_comparator(0,2)
#     thi = Comp.make_comparator(1,2)

#     Bigger_Filter = add(fir, Bigger_Filter)
#     Bigger_Filter = add(sec, Bigger_Filter)
#     Bigger_Filter = add(thi, Bigger_Filter)
    
#     >>> is_sorting(Small_Filter)
#     False

#     >>> is_sorting(Bigger_Filter)
#     True
#     """
    
#     return len(out(f)) == (size(f) + 1)

def is_sorting(f: Filter) -> bool:
    """
    Checks if the network in the filter is a sorting network.

    The slow version that is paired with the fast version of add()

    DOCTEST
    n = 3
    
    Small_Filter = make_empty_filter(n)
    
    fir = Comp.make_comparator(0,1)
    sec = Comp.make_comparator(0,2)
    thi = Comp.make_comparator(1,2)

    Bigger_Filter = add(fir, Bigger_Filter)
    Bigger_Filter = add(sec, Bigger_Filter)
    Bigger_Filter = add(thi, Bigger_Filter)
    
    >>> is_sorting(Small_Filter)
    False

    >>> is_sorting(Bigger_Filter)
    True
    """
    
    if len(out(f)) < 2:
        return True

    else:
        all_sorted = True
        
        i = 1

        while i < (len(out(f)) - 1) and all_sorted:
            j = 0

            while j < (len(out(f)[i]) - 1) and all_sorted:

                if out(f)[i][j] > out(f)[i][j+1]:
                    all_sorted = False    
                
                else:
                    j = j + 1
            
            i = i +1
        
        return all_sorted
                    
            


