"""
network.py
Made by H8G03: Valdemar, Mathias og Hlynur
"""

from dataclasses import dataclass
import comparator as Comp 
from permutations import * #Note: We made this module ourselves

"""
We start by importing the dataclass functionality, 
the comparator module and our own permutations module.
"""

@dataclass
class Network(): 
    """
    The network is implemented as a dataclass,
    whose only property is to create a list of comparator objects.
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
    Appends a comparator c to the Network, net. 
    
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
    Returns the largest j-value in the network. The main difference in not using
    max.channel() from comparator.py is that we avoid
    non-standard Comparators.

    Instead it uses get_j() from comparator as an auxiliary function
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
    network, the following for-each loop is skipped.
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
    Com_1 = comparator_1.make_comparator(7,1)
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
    If the for-each loop reached the end of the list without ever finding at
    least one non-standard Comparator then the function returns True.
    
    None are False => All are True
    """
    return True

def apply(net: Network, w: list[int]) -> list[int]:
    """
    Sorts a single list of integers using comparators
    in a network.

    Requirement:
    size(net) > 0
    len(w) > 0

    DOCTEST
    net = empty_network()
    Com_1 = Comp.make_comparator(1,3)
    Com_2 = Comp.make_comparator(2,3)

    w = [1,2,4,3]

    append(Com_1, net)
    append(Com_2, net)

    >>> apply(net, w)
    [1, 2, 3, 4]
    """
    
    for i in range(0, size(net)):
        """
        For every Comparator in the network, apply the 
        Comparators on the list, so every Comparator is
        used at least once  
        """
        Comp.apply(net.network[i],w)
    
    return w

def outputs(net: Network, w: list[list[int]]) -> list[list[int]]:
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

    append(Com_1,net)
    append(Com_2,net)
    
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

        """
        Python supports the datatype sets which are unorderd
        collections of elements with no duplicates.
        Python can convert a list to a set using the set()
        function which will also remove any duplicate elements.

        But by converting the set back to a list using the
        list() function, we essentially get the original list
        without duplicates, since we didn't change the order
        of the set or modified it in any other way.

        w[i] = set(w[i])
        w[i] = list(w[i])
        """
    return w


def all_outputs(net: Network, n: int) -> list[list[int]]:
    """
    Returns all permutations of 0 and 1 of n length,
    essentially the same as counting from 0 to n in binary,
    and then sortes them and removes repeats.

    Requirement:
    n > 0

    DOCTEST
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
    Checking the minimum criteria for the network.
    """
    if len(net.network) == 0:
        return False

    if max_channel(net) != (size-1) : #Code using 0-indexing
        return False
    
    """
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
            if permu[i][j] > permu[i][j+1]: 
                return False
    return True

def to_program(net: Network, var: str, aux: str)-> list[str]:
    """
    Returns a list of instructions that simulates the Comparator network.

    DOCTEST
    net = empty_network()
    Com_1 = Comp.make_comparator(0,1)
    Com_2 = Comp.make_comparator(2,3)
    Com_3 = Comp.make_comparator(0,2)
    append(Com_1, net)
    append(Com_2, net)
    append(Com_3, net)
    >>> to_program(Net1, var, aux)
    [['if var[0] > var[1]:', 'aux = var[0]', 'var[0] = var[1]', 'var[1] = aux'],
    ['if var[2] > var[3]:', 'aux = var[2]', 'var[2] = var[3]', 'var[3] = aux'],
    ['if var[0] > var[2]:', 'aux = var[0]', 'var[0] = var[2]', 'var[2] = aux']]
    """
    # Note: The output from this program can be run by the command exec()
    # and should result in the same execution as apply()
    returned_list = []

    # Iterates through the entire network
    for i in range(size(net)): 
         # Iterates through the list from to_program() in comparator.py
        for j in range(len(Comp.to_program(net.network[i], var, aux))): 
            # Appends each line as a new element in returned_list
            returned_list.append(Comp.to_program(net.network[i], var, aux)[j]) 
            # Next line is only needed if you need to be able to run the code
            # Creates a new line to seperate each output from to_program() in comparator.
            returned_list.append("\n")
    return returned_list
