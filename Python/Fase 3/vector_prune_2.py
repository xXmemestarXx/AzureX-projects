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
import filter_new as Filt
import generate_new as Gene
import prune as Prun

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

def make_comparison_vector(n: int) -> list[int]:
    """
    Quickly makes the vector that would result
    from adding all the vectors in the
    outputs of a sorting network for n channels
    
    reg:
    n > 0
    """
    res = []
    for i in range(1,n+1):
        res.append(i)
    return res

def filter_vector(f: Filt.Filter):
    """
    Takes a Filters outputs and returns a 
    new vector.

    DOCTEST
    Filt.out(Filter)=  [[0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0],
                        [1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 1],
                        [1, 0, 0, 1, 1],
                        [0, 0, 1, 1, 1],
                        [1, 0, 1, 1, 1],
                        [0, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1]]
    >>> filter_vector(Filter)
    [4, 2, 4, 8, 7]          
    """
    return add_vectors(Filt.out(f))

def sqr_eu_dist(cv: list,v: list) -> int:
    """
    Calculates the square distance between two
    vector using Pythagoras' theorem
    """
    return sum(list(map(lambda x,y: (x-y)**2,cv,v)))

def all_dis(cv: list[int],fv: list[Filt.Filter]) -> list[int]: 
    """
    Calculates distances between a constant vector and
    all the vectors generated from a list of Filters
    
    DOCTEST

    filt_test = Filt.make_empty_filter(5)
    filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)
    filt_test = Filt.add(Comp.make_comparator(1,4), filt_test)
    
    filt_test2 = Filt.make_empty_filter(n)
    filt_test2 = Filt.add(Comp.make_comparator(2,4), filt_test2)
    filt_test2 = Filt.add(Comp.make_comparator(1,4), filt_test2)
    filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)

    fv = [filt_test,filt_test2]
    cv = make_comparison_vector(5)
    
    >>> all_dis(cv,fv)
    [291, 151]
    """
    all_distances = []
    for i in range(0,len(fv)):
        all_distances.append(sqr_eu_dist(cv,filter_vector(fv[i])))
    return all_distances

def sort_dist_and_filt(v: list[int],w: list[Filt.Filter]) -> list[Filt.Filter]:
    """
    Bubble sorts the Filter according to their distances from the
    comparison vector. Their distances is in another list
    and not part of the Filter data structures themselves,
    therefore two lists are required.

    The main difference from bubble sort is that we sort two lists

    req:
    len(v) = len(w) 
    len(v), len(w) > 0

    DOCTEST:

    v = [1,5,8,3]
    w = [Filter_1,Filter_2,Filter_3,Filter_4]

    >>> sort_dist_and_filt(v,w)
    [Filter_1,Filter_4,Filter_2,Filter_3]
    """
    dis = v[0:] #to avoid changing input list
    fil = w[0:] #to avoid changing input list

    for i in range(0,len(fil)): #v and w should be equally long
        for j in range(0,(len(fil)-1)-i):
            if dis[j] > dis[j+1]:
                dis[j], dis[j+1] = dis[j+1], dis[j]
                fil[j], fil[j+1] = fil[j+1], fil[j]
    return fil

def vector_prune(n: int, w: list[Filt.Filter]):
    """
    Makes vector from the outputs in the list of Filter,
    whereafter the function calculates the distances between 
    the vectors and a constant vector created from a sorting 
    networks outputs. 

    Then sortes the Filters according to their distances from 
    the comparison vector and returns the first fraction of them
    determined by the denominator
    """
    cov = make_comparison_vector(n)

    dis = all_dis(cov,w)
    
    pru = sort_dist_and_filt(dis,w)

    # Slices the list invers proportionally, so we keep fewer
    # Filters the longer the list of Filter gets
    return pru[0: int(1/(len(pru))*100000)]