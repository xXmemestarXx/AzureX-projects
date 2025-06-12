"""
Importing 3rd party libaries
"""
import functools as Func
from dataclasses import *

"""
Importing our own modules
"""
import comparator2 as Comp
import network as Netw
import filter as Filt
import generate2 as Gene

F1 = Filt.add(2,Filt.make_empty_filter(3))
F2 = Filt.add(5,Filt.make_empty_filter(3))
F3 = Filt.add(8,Filt.make_empty_filter(3))

all_filters = [F1,F2,F3]

for i in range(0,len(all_filters)):
    print(f"Filter {i+1} network contains {Filt.net(all_filters[i])} and its outputs are {Filt.out(all_filters[i])}\n")

new = Gene.extend(all_filters,3)

print("After Extending")

for i in range(0,len(new)):
    print(f"Filter {i+1} network contains {Filt.net(new[i])} and its outputs are {Filt.out(new[i])}\n")


