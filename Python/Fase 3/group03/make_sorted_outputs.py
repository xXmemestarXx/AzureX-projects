"""
make_sorted_outputs.py

Written by Valdemar H8G03

DM574 Exam project
"""

"""
Importing 3rd party libaries
"""
from dataclasses import *

"""
Importing our own and our lecturer's modules
"""
import comparator as Comp
import network as Netw
import filter as Filt
import generate as Gene
import prune as Prun

def make_sorted_outputs(n: int):
    """
    makes a sorted lists of lists of ints that
    are equal to the outputs in a sorting network
    for n amount of channels
    """
    if n == 0:
        return []
    else:
        base = [0 for i in range(0,n)]

        #print(base)

        whole = [base]

        return  whole + _make_sorted_outputs(whole[0],n-1)

def _make_sorted_outputs(v: list[int], n: int):
    """
    Auxillary function which takes a list of 0's and
    changes the n'th index to 1 and then calls itself
    """
    new_base = v[0:]
    new_base[n] = 1
    new_n = n-1

    #print(new_base)

    if new_n == -1:
        return [new_base]
    else:
        return [new_base] + _make_sorted_outputs(new_base,new_n)

# print(make_sorted_outputs(0))

# print(make_sorted_outputs(1))

# print(make_sorted_outputs(2))

# print(make_sorted_outputs(3))

# print(make_sorted_outputs(4))
