"""
network_finder.py

Written by Hlynur, Mathias and Valdemar H8G03

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
import filter_new as Filt
import generate_new as Gene
import prune as Prun


"""
network_finder is essentially a small Command Line Interface program, or CLI.
Therefore the user interface, UI, and the user experience, UX, needs to be taking
into acoount. The simplest way to do this is by printing guiding helpful messages,
so the user knows when and how they are using the program wrong. 
"""

def make_sorting_network(f: list[Filt.Filter], n: int, i: int) -> Filt.Filter:
    """
    Checks if there is one or more sorting networks in the filter list, and then returns the first sorting network. 
    """
    if any(list(map(Filt.is_sorting, f))):
        # for i in range(0,len(list(filter(lambda x: Filt.is_sorting(x) == True, f)))):
        #     print(list(filter(lambda x: Filt.is_sorting(x) == True, f))[i])
        return list(filter(lambda x: Filt.is_sorting(x) == True, f))[0]
    
    i = i + 1
    extended_filters = Gene.extend(f, n)
    clean_list = Prun.prune(extended_filters, n)
    
    print(f"Iteration: {i}")
    print(f"EXTENDED: {len(extended_filters)}, PRUNED: {len(extended_filters)-len(clean_list)}, REMAINDER: {len(clean_list)}")
    
    print("")

    #return make_sorting_network(extended_filters, n, i)
    return make_sorting_network(clean_list, n, i)

done = False

while not done:
    print(
        """
        ._______________________________________.
        |                                       |
        |   Welcome to Network Finder Program   |
        |     by Hlynur, Mathias & Valdemar     |
        `_______________________________________´
        """)
    print("Tip: Time needed to calculate is proportional to amount of channels ")

    channel_amount = int(input("Please enter how many channels you want to sort: "))

    while 1 > channel_amount:
        """
        Checks wheter the input is valid number or not
        """
        if 0 >= channel_amount:
            print("Please enter a number greater than zero")

        else:
            print("Invalid input")
        channel_amount = int(input())


    all_filters = [Filt.make_empty_filter(channel_amount)]

    print(f"Finding a sorting network for {channel_amount} channels... \n")

    sorting_network = make_sorting_network(all_filters, channel_amount, 0)

    print(f"Found a sorting network for {channel_amount} channels with size {Netw.size(Filt.net(sorting_network))} \n")

    print(f"An inplementation of the sorting network in Python would look like: \n")

 
    program_string = Netw.to_program(Filt.net(sorting_network),'','')
    
    for i in range(0,len(program_string)):
        print(program_string[i])


    done = True

