"""
network_finder.py

Written by Mathias, Hlynur and Valdemar H8

DM574 Examprojekt
"""

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
import permutations as Perm
import filter_rev2 as Filter
"""
network_finder is essentially a small Command Line Interface program, or CLI.
Therefore the user interface, UI, and the user experience, UX, needs to be taking
into acoount. The simplest way to do this is by printing guiding helpful messages,
so the user knows when and how they are using the program wrong. 
"""

print(
    """
    ._______________________________________.
    |                                       |
    |   Welcome to Network Finder program   |
    |     by Mathias, Hlynur & Valdemar     |
    `_______________________________________´
    """)


print("Please enter how many channels you want to sort:")

print("It is recommended to not try sorting 5 or more channels")



channel_amount = int(input())

while 1 > channel_amount:
    """
    Checks wheter the input is valid number or not
    """

    if 0 >= channel_amount:
        print("Please enter a number greater than zero")

    else:
        print("Invalid input")
    channel_amount = int(input())

all_filters = [Filter.make_empty_filter(channel_amount) for x in range(0,10)]
print("These are the filter generated")
for i in range(0,len(all_filters)):
    print(f"Filter {i+1} network contains {all_filters[i].net.network} and its outputs are {all_filters[i].outputs}\n")

