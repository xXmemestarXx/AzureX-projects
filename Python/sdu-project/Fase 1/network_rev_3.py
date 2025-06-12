"""
network.py rev. 2

lavet af H8G03: Valdemar, Mathias og Hlynur

dokumentation er på dansk, men skal omskrives til engelsk

"""

from dataclasses import dataclass
from functools import *
import comparator_rev_3  as Comp



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
    Returns the maximum channel, aka largest number, in the network
    as an integer. 
    
    Uses max.channel() from comparator as an auxiliary function
    Therefore Comparator.py needs to be imported.

    tested in test_network_rev_1.py

    Requirement: 
    size(net) > 0

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

    max = Comp.max_channel(net.network[0])
    """
    We start by equating the maximum channel of the network to
    the maximum channel of the first comparator of the network.

    This also ensures that if there is only one comparator in the 
    network, the following for-loop is skipped.
    """


    for i in range(1,size(net)):
        """
        Thereafter we check the maximum channel of each Comparator one-by-one
        except the first one, since we already checked it.
        """

        if Comp.max_channel(net.network[i]) > max:
            """
            If the function finds a bigger number via the for-loop 
            and if-statement, it overwrites the previous maximum channel
            and continues to check the other Comparators
            """
            max = Comp.max_channel(net.network[i])


    return max



def is_standard(net:object) -> bool:
    """
    Checks whether the input Network only
    contains standard comparators or not

    Note:
    A standard comparator is a comparator where
    its j-value is larger than its i-value
    
      
    Uses is.standard() from comparator-module as an 
    auxiliary function. Therefore Comparator.py
    needs to be imported.

    Requirement:
    size(net) > 0

    Doc_Test:
    Net_1 = empty_network()
    Com_1 = comparator_1.make_comparator(7,-1)
    Com_2 = comparator_1.make_comparator(3,5)
    append(Com_1,Net_1)
    append(Com_2,Net_1)
    
    >>>is_standard(Net_1)
    false
    """

    for i in range(0,size(net)):
        """
        We go through the list of Comparators and check one-by-one if they
        are standard or not. If at least one of them is non-standard then
        the whole function returns false.
        """
        if Comp.is_standard(net.network[i]) is False:
            return False
    
    """
    If the for-loop reached the end of the list without ever finding at
    least one non-standard Comparator then the function returns True.
    
    None are False => All are True
    """
    return True

def apply(net: object, w: list[int]) -> list[int]:
    """
    Sorts a single list of integers using comparators
    in a network.

    requirement:
    size(net) > 0
    len(w) > 0

    """
    for i in range(0,size(net)):
        """
        For every Comparator in the network, apply the 
        Comparators on the list, so every Comparator is
        used at least once  
        """
      
        Comp.apply(net.network[i],w)
    
    return w


def outputs(net : object, w : list[list[int]]) -> list[int]:
    """
    Returns a sorted list of lists containing no duplicates
    The list themselves are not sorted
    """

    for i in range(0,len(w)):
        apply(net,(w[i]))
        w[i] = list(set(w[i]))

    return (w)


def is_sorting(net : object,size :int) -> bool:
    if size(net) < 1 or is_standard(net) == False:
        return False
    
    # osv.