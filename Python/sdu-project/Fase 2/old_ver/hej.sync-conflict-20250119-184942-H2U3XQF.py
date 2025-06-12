"""
Importing 3rd party libaries
"""
import functools as Func
from dataclasses import *

"""
Importing our own modules
"""
import comparator as Comp
import network as Netw
import filter as Filt
import generate as Gene


# lst = [1, 2, 3, 4, 5]

# def add(a,b):
#     c = a+b
#     return c

# p = Func.reduce(add, 
#                 list(
#                     map(lambda i: 
#                         list(
#                             map(lambda j:
#                                 (i, j),
#                                 lst),
#                         )
#                         ,
#                         lst
#                         )
#                     )

#                 )

# print(p)


F1 = Filt.add(2, Filt.make_empty_filter(3))
F2 = Filt.add(5, Filt.make_empty_filter(3))
F3 = Filt.add(8, Filt.make_empty_filter(3))

print(f"{F1} \n")


all_filters = [Filt.make_empty_filter(3) for x in range(0,2)]

all_filters = [F1,F2,F3]


for i in range(0,len(all_filters)):
    print(f"Filter {i+1} network contains {Filt.net(all_filters[i])} and its outputs are {Filt.out(all_filters[i])}\n")


def get_all_min_max(net: list) -> tuple:
    res = []
    for i in range(0,Netw.size(net)):
        res.append((Comp.min_channel(net[i]),Comp.max_channel(net[i])))
    return res


new = Gene.extend(all_filters,3)

print("After Extending")

for i in range(0,len(new)):
    print(new[i])
    
    #print(f"Filter {i+1} network contains {Comp.min_channel(Filt.net(new[i][0])),Comp.max_channel(Filt.net(new[i][0]))} and its outputs are {Filt.out(new[i])} \n")
    

    #print(f"Filter {i+1} network contains {Filt.net(new[i])} and its outputs are {Filt.out(new[i])} \n")    

    #print(f"Filter {i+1} network contains {get_all_min_max(Filt.net(new[i]))} and its outputs are {Filt.out(new[i])} \n")





