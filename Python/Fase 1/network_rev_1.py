"""
network.py rev. 1

lavet af H8G03: Valdemar, Mathias og Hlynur

dokumentation er på dansk, men skal omskrives til engelsk

"""

from dataclasses import dataclass
from functools import *
"""
Starter med at importere en masse værktøjer.
Ved ikke hvilke funktionaliteter der skal bruges eller kan undværes,
så derfor importeres alting fra biblotekterne
"""

@dataclass
class Network(): 
    """
    I første udgave af network.py er Network inplementeret som en 
    Dataclass, hvis eneste egenskab er en liste af Comparator objekter.
    
    I næste revision kan Network f.eks. være en Stack, men på nuværemde tidspunkt
    (23.10.2024) kan forskellen mellem inplementationerne ikke skelnes  
    """
    network : list

def to_string(Network:object) -> str:
    """
    Writes the contents of a Network object to a String
    Useful for testing

    tested in test_network_rev_1.py

    doc_test:
    Network.network = [obj_1,obj_2]
    >>> '[obj_1,obj_2]'

    """ 
    return (f"{Network.network}")


def empty_network() -> dataclass:
    """
    Creates an empty Network object that only contains an empty list

    tested in test_network_rev_1.py

    """
    return Network([])

def append(c: any , net :object) -> None:
    """
    Appends a comparator, c, in the Network, net. 
    
    Iterates on net and does not a copy of it in memory.

    tested in test_network_rev_1.py

    doc_test:
    
    append(Comparator_1,Network)
    append(Comparator_2,Network)
    
    to_string(Network)
    
    >>> [Comparator_1,Comparator_2]
    """
    net.network.append(c)

def size(net : object) -> int:
    """
    Returns the amount of Comparators in a Network 
    in the form of an integer

    tested in test_network_rev_1.py

    doc_test:
    Network.network = [Comparator_1,Comparator_2]
    size(Network)
    >>> 2

    """
    return len(net.network)

def max_channel(net : object) -> int:
    """

    To Do

    Returns the maximum channel, aka largest number, in the network
    as an integers. 
    Uses max.channel() from comparator as an auxiliary function

    Doc_Test:
    
    Comparator_1.i = 2
    Comparator_1.j = 4
    
    Comparator_2.i = 1
    Comparator_2.j = 5

    Comparator_3.i = 2
    Comparator_3.j = -1

    append(Comparator_1,Network)
    append(Comparator_2,Network)
    append(Comparator_3,Network)
        
    max_channel(Network)
    >>> 5
    """

    last_comparator = net.network[-1]

    return 0