"""
Network.py rev. 3
Made by H8G03: Valdemar, Mathias og Hlynur
"""

from dataclasses import dataclass
import comparator_rev_7 as Comp
from permutations import * #Note: We made this module ourselves

"""
We start by importing the dataclass functionality, and the comparator module
"""

@dataclass
class Network(): 
    """
    In the first revision of Network.py, the network is implemented as a
    dataclass, whose only property is to create a list of comparator objects.
    
    In the next revision there is a possibility that the implementetion uses a Stack. 
    At the current time (23.10.2024) the differnece in implentation is not yet known.
    """
    network: list

def to_string(net: Network) -> str:
    """
    Writes the contents of a Network object to a String
    Note: Useful for testing

    DOCTEST
    >>> net.network = [obj_1, obj_2]
    '[obj_1, obj_2]'
    """ 
    return (f"{net.network}")


def empty_network() -> dataclass:
    """
    Creates an empty Network object that only contains an empty list
    """
    return Network([])

def append(c: Comp, net: Network) -> None:
    """
    Appends a comparator c in the Network, net. 
    
    Iterates on net and does not make a copy of it in memory.

    DOCTEST
    >>> append(Comparator_1,Network)
    >>> append(Comparator_2,Network)
    Network = [Comparator_1, Comparator_2]
    """
    net.network.append(c)

def size(net: Network) -> int:
    """
    Returns the amount of Comparators in a Network 
    in the form of an integer

    DOCTEST
    Network.network = [Comparator_1,Comparator_2]
    >>> size(Network)
    2
    """
    return len(net.network)

def max_channel(net: Network) -> int:
    """
    Rev.1
    Returns the maximum channel, aka largest number, in the network
    as an integer. 
    
    Uses max.channel() from comparator as an auxiliary function
    Therefore Comparator.py needs to be imported.

    Rev.2
    Returns the largest j-value in the network. The main difference from
    using max.channel() from comparator.py is that we avoid
    non-standard Comparators.

    Uses get_j() from comparator as an auxiliary function
    Therefore Comparator.py needs to be imported.

    Requirement: 
    size(net) > 0

    DOCTEST
    Comparator_1.i = 2
    Comparator_1.j = 4
    
    Comparator_2.i = 1
    Comparator_2.j = 5

    Comparator_3.i = 2
    Comparator_3.j = -1

    append(Comparator_1,Network)
    append(Comparator_2,Network)
    append(Comparator_3,Network)
    
    >>> max_channel(Network)
    5
    """

    max = Comp.get_j(net.network[0])

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

        if Comp.get_j(net.network[i]) > max:
            """
            If the function finds a bigger number via the for-loop 
            and if-statement, it overwrites the previous maximum channel
            and continues to check the other Comparators
            """
            max = Comp.get_j(net.network[i])
    return max

def is_standard(net: Network) -> bool:
    """
    Checks whether the input Network only
    contains standard comparators or not

    Note:
    A standard comparator is a comparator where
    its j-value is larger than its i-value
    
      
    Uses is.standard() from comparator module as an 
    auxiliary function. Therefore Comparator.py
    needs to be imported.

    Requirement:
    size(net) > 0

    DOCTEST
    Net_1 = empty_network()
    Com_1 = comparator_1.make_comparator(7,-1)
    Com_2 = comparator_1.make_comparator(3,5)
    append(Com_1,Net_1)
    append(Com_2,Net_1)
    
    >>> is_standard(Net_1)
    False
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

def apply(net: Network, w: list[int]) -> list[int]:
    """
    Sorts a single list of integers using comparators
    in a network.

    requirement:
    size(net) > 0
    len(w) > 0

    DOCTEST
    net = empty_network()
    Com_1 = Comp.make_comparator(-7,19)
    Com_2 = Comp.make_comparator(3,-5)
    Com_3 = Comp.make_comparator(3,42)

    w = [1,4,7,4,767,8,5,654,454,6,8,5,43,43,315563]

    append(Com_5,Net_6)
    append(Com_6,Net_6)
    append(Com_7,Net_6)
    >>> apply(net, w)
    [1, 4, 4, 5, 5, 6, 7, 8, 8, 43, 43, 454, 654, 767, 315563]
    """
    for i in range(0, size(net)):
        """
        For every Comparator in the network, apply the 
        Comparators on the list, so every Comparator is
        used at least once  
        """
        Comp.apply(net.network[i],w)
    
    return w

def outputs(net: Network, w: list[list[int]]) -> list[int]:
    """
    Returns a sorted list of lists containing no duplicates
    The list themselves are not sorted

    Requirement:
    size(net) > 0
    len(net) > 0    

    DOCTEST
    net = empty_network()
    
    Com_1 = Comp.make_comparator(0,1)
    Com_2 = Comp.make_comparator(1,2)
    Com_3 = Comp.make_comparator(0,2)
    
    append(Com_1,net)
    append(Com_2,net)
    append(Com_3,net)
    
    v = [[36,25,25],[36563236,63425,4433660]]

    >>> outputs(net, v)
    [[25,25,36],[63425,4433660,36563236]]
    """

    for i in range(0,len(w)):
        """
        Sorts the individual lists inside the w
        by using apply() as an auxiliary function
        """
        apply(net,(w[i]))

        """
        Depends on if we want to also remove the duplicate
        numbers in the list
        """
        
        # """
        # Python supports the datatype sets which are unorderd
        # collections of elements with no duplicates.
        # Python can convert a list to a set using the set()
        # function which will also remove any duplicate elements.

        # But by converting the set back to a list using the
        # list() function, we essentially get the original list
        # without duplicates, since we didn't change the order
        # of the set or modified it in any other way.
        # """
        # w[i] = set(w[i])
        # w[i] = list(w[i])

    return (w)


def all_outputs(net: Network, n: int) -> list[list[int]]:
    """
    Returns all permutations of 0 and 1 of n length,
    essentially the same as counting from 0 to n in binary,
    and then sortes them and removes repeats.

    Requirement:
    n > 0

    Doc_Test:
    >>> all_outputs(1)
    [[0],[1]]

    >>> all_outputs(3)
    [[000],[001],[010],[011],[100],[101],[111]]
    """
    permu = permutations(n)

    permu = outputs(net,permu)

    permu_no_dupe = []

    for i in range(0,len(permu)):
        if permu[i] not in permu_no_dupe:
           permu_no_dupe.append(permu[i]) 

    return permu_no_dupe


def is_sorting(net: Network, size: int) -> bool:
    """
    
    We will refer the variable size to letter n
    
    Checks wheter a sorting network is able to correctly sort
    a network with n amount of channels with the comparators
    it has. 

    To achieve this there are (at least) main two strategies.
        
        1:
        Check whether the network have all the neccesay
        comparators to correctly sort n amount of channels.
        
        This method allows the network to contain reduntant
        comparators but that isn't relevant to question of
        if a specific network can sort n amount of channels.
        
        This is theorectally faster but the stategy has a
        major downside. The order of Comparatoralls does matter
        in Networks larger than 1. Networks also need
        multiple copies of the same Comparator, altough in 
        different places, to correctly sort Networks larger
        than 1.
        
        One could check if network have all the neccesay
        comparators in the correct order but would be very
        labour intensive since there multiple orders


        2:
        Try to sort all permutations of 0's and 1's of
        n amount of digigts using the network in question
        and check if the network sorted it correctly or not.

        This method also allows the network to 
        contain non-standard or reduntant Comparators
        that doesn't affect the final output

        This strategy is very labour intensive, since
        we both need to call outputs() and all_outputs()
        and then one-boy-one check the output.
    
    
    DOCTEST
    
    Net_1 = empty_network()
    Com_1 = Comp.make_comparator(1,3)
    Com_2 = Comp.make_comparator(2,4)
    append(Com_1,Net_1)
    append(Com_2,Net_1)
    
    Net_2 = empty_network()
    Com_3 = Comp.make_comparator(0,1)
    com_4 = Comp.make_comparator(0,2)
    Com_5 = Comp.make_comparator(1,2)
    append(Com_3,Net_2)
    append(Com_4,Net_2)
    append(Com_5,Net_2
    
    >>> is_sorting(Net_1, 3)
    False
    
    >>> is_sorting(Net_2, 3)
    True
    """
    

    """
    There are some minimum criteria for valid network:

        1: The network should not be empty

        2: The network should only contain standard comparators,
            but it can contain non-standard Comparators if
            their outputs are fully overwritten by standard
            Comparators.

        3: The Networks max_channel() value should 
            be equel to amount of channels subtracted by 1 
            (minus 1 because of 0-indexing). If the value
            is less than the amount of channels (minus 1) 
            then the network won't be able to sort the 
            overlooked values and return a partially sorted
            list. If the value is greater than the amount 
            of channels (minus 1) the network will try 
            to place values in nonexistant channels 
            which will crash the program and not produce
            anything.

    If the network does not furfill all the requirements
    then it will not to able correctly sort.
    """
    if len(net.network) == 0:
        return False

    # if is_standard(net) == False:
    #     return False

    if max_channel(net) != (size-1) : #Code using 0-indexing
        return False


    # """
    # Strategy 1

    # First we make a new network that contains all the 
    # comparators that are neccessary to sort n amount of
    # channels.

    # We will use std_comparators()as a auxillary function
    # """
    
    # new_net = Comp.std_comparators(size)

    # """
    # Thereafter we will check if the new network containing all
    # the neccesary comparators is a subset of the network we
    # want to check.

    # Python supports checking whether a list is a subset
    # of a nother list by using the <= operater.
     
    # Unfortunately to be able to use the <= operater
    # the elements need to be in same order in the lists
    # which isn't neccesary in this situation

    # To deal with this we can converts the list of
    # comparators to sets which by definitiona are
    # unordered as mentioned in the documentation of outputs()

    # Additionally Python has a inbuilt function for sets
    # called issubset() which return a boolean.

    # But there is a problem. For a list to be converted to a set
    # its contents needs to be hashable and immutable, which list
    # are not.

    # Therefore we also need to extract the contents of the
    # comparators to list and put them inside tuple which
    # are immutable.
    # """
  
    # old = set()

    # new = set()


    # for c in range(0,len(net.network)):
    #     old.add(Comp.get_i_and_j(net.network[c]))
    
    # for c in range(0,len(new_net)):
    #     new.add(Comp.get_i_and_j(new_net[c]))


    # print(old)
    # print(new)

    # return new.issubset(old)

    """
    Strategy 2

    First we create all permutations of 0 and 1
    of n length and place it in a list
    """
    permu = all_outputs(net,size)

    """
    We check if the list of lists of integers are
    sorted correctly be checking every integer
    one-by-one. If a previous value is larger
    than the following value then the list
    is sorted incorrectly. If all previous values
    are less than the following values then the list
    is sorted correctly.
    """
    for i in range(0,len(permu)-1):
        
        for j in range(0,len(permu[i])-1):
            
            if permu[i][j] > permu[i+1][j+1]: 
                return False
    
    return True



