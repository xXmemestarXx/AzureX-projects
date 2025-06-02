"""
vector_prune.py

Written by Valdemar H8G03

DM574 Exam project
"""

"""
Importing 3rd party libaries
"""
from dataclasses import *
import functools as Func

"""
Importing our own and our lecturer's modules
"""
import comparator as Comp
import network as Netw
import filter as Filt
import generate_new as Gene
import prune as Prun
import make_sorted_outputs as MSOP


def add_vectors(v: list[list[int]]) -> list[int]:
    """
    Adds all the vectors in v and returns a single vector

    reg:
    all vectors need to be the same length

    len(v) > 0
    """
    new_v = [0 for x in range(0,len(v[0]))]
    
    i = 0

    while i < len(v):
        j = 0

        while j < len(v[0]):
            new_v[j] = new_v[j] + v[i][j]
            j = j + 1
        
        i = i + 1
        
    return new_v


def make_comparison_vector_slow(n: int) -> list[int]:
    """
    Takes the sorted outputs of a sorting network for 
    n channel and turns them into a single vector
    
    reg:
    n > 0
    """
    outp = MSOP.make_sorted_outputs(n)
    vect = add_vectors(outp[1:]) #since the first vector is 0's
    return vect

def make_comparison_vector(n: int) -> list[int]:
    """
    Quickly makes the vector that would result
    from adding adding all the vectors in the
    outputs of a sorting network for n channels
    
    reg:
    n > 0
    """
    res = []
    for i in range(1,n+1):
        res.append(i)
    return res

def filter_vector(f: Filt.Filter):
    return add_vectors(Filt.out(f))

def all_filter_vectors(v: list[Filt.Filter]):
    return[filter_vector(f) for f in v]


def sqr_eu_dist(cv: list,v: list) -> int:
    return sum(list(map(lambda x,y: (x-y)**2,cv,v)))


def all_dis(cv: list[int],fv: list[Filt.Filter]):
    
    all_distances = []
    for i in range(0,len(fv)):
        all_distances.append(sqr_eu_dist(cv,filter_vector(fv[i])))
    return all_distances

# TODO
# def sorted_distances(fv: list[int]) -> list[tuple[int]]:
#     sort_dist = []
#     i = 0
#     while i < len(fv):
#         j = 0
#         while j < len(sort_dist):
#             if 

#     return 0
