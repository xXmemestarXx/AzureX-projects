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
import filter_new as Filt
    
def extend(w: list[Filt.Filter], n: int) -> list[Filt.Filter]:
    """
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
    stdComp = Comp.std_comparators(n)[0:]

    """
    We need to use the list() function multiple
    times since Python's version of the map
    function returns an object.
    """
    
    # carte_prod = []
    # i = 0
    
    # while i < len(w):
            
    #         j = 0

    #         while j < len(w):
                
    #             if not Filt.is_redundant(stdComp[j],w[i]):
    #                 new = Filt.add(stdComp[j],w[i])
    #                 carte_prod.append(new)
                
    #             j = j + 1
            
    #         i = i + 1

    # return carte_prod

    return Func.reduce(
            lambda x, y: x + 
                    list(map(lambda c: Filt.add(c, y),
                    filter(lambda c: not Filt.is_redundant(c, y),stdComp
                    )
                )
            ),
            w,
            [Filt.make_empty_filter(n)]
        )



