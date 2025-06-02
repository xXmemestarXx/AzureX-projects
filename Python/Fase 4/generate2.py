"""
generate.py

Written by Hlynur, Mathias and Valdemar H8G03

DM574 Exam project
"""

# THIS VERSION USES IMPERATIVE PROGRAMMING INSTEAD

"""
Importing 3rd party libaries
"""
import functools as Func
from dataclasses import *

"""
Importing our own and our lecturer's modules
"""
import comparator2 as Comp
import network as Netw
import filter_new as Filt

"""
Importing definitions of data structures
"""
Comparator = int
Network = list[Comparator]
Filter = list[Netw.Network, list[list[int]]]
    
def extend(w: list[Filter], n: int) -> list[Filter]:
    """
    Preconditions: n > 0 and len(w) > 0

    Adds all non-redundant standard comparators for
    n amount of channels to the Filters in 
    the input list, w. 

    DOCTEST
    n = 2
    filt_test = Filt.make_empty_filter(n)
    w = [filt_test]
    filt_test2 = Gene.extend(w, n)
    >>> filt_test2 = extend(w,2)
    [Filter(n=[2], out=[[0, 0], [0, 1], [1, 1]], size=2)]
    """

    # Gets all std comp

    
    stdComp = Comp.std_comparators(n)
    
    res = []

    for x in range(len(w)):
      for y in range(len(stdComp)):
        if not Filt.is_redundant(stdComp[y],w[x]):
            res.append(Filt.add(stdComp[y],w[x]))
    return res
  