"""
generate.py

Written by Hlynur, Mathias and Valdemar H8G03

DM574 Exam project
"""

"""
Importing 3rd party libaries
"""
import functools as Func
from dataclasses import *

"""
Importing our own and our lecturer's modules
"""
import comparator as Comp
import network as Netw
import filter as Filt

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

    This is equal to calculating a subset of the
    cartesian product of w and all standard 
    comparators for n amount of channels

    DOCTEST
    n = 2
    filt_test = Filt.make_empty_filter(n)
    w = [filt_test]
    filt_test2 = Gene.extend(w, n)
    >>> filt_test2 = extend(w,2)
    [Filter(n=[2], out=[[0, 0], [0, 1], [1, 1]], size=2)]
    """
    
    """
    Start by getting all the standard Comparators
    """
    stdComp = Comp.std_comparators(n)

    """
    The following map functions makes a subset
    of the cartesian product of the input Filters
    and all standard comparators for n amount of
    channels. It is a subset since we only keep
    the non-redundant comparators and the original
    Filters.

    We need to use the list() function multiple
    times since Python's version of the map
    function returns an object.
    """
    #carte_prod = list(map(lambda f: 
    #list(map(lambda c: _check_and_add(c,f),stdComp)),w))                                   
  
    carte_prod = list(map(lambda f: list(map(lambda c: Filt.add(c,f)
                 if not Filt.is_redundant(c,f) else [],stdComp)),w))                                   
    """
    Since the lambda function needs to always return some
    some type value, the lambda function will return
    the empty list when a Comparator is redundant. If we
    removed the line then the auxillary function would
    return None if a Comparator is redundant.
    """

    combined_filters = Func.reduce(lambda x,y: x+y,carte_prod)
    
    """
    Python always requires an else clause when using
    if-statements in a map. There _add_and_check()
    returns a empty list when a Comparator is redundant. We
    remove all the 0's using the filter function
    """
    extended_filters =  list(filter(lambda x: x != [],combined_filters))

    return extended_filters