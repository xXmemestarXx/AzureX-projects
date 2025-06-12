import functools as func

def permutations(n) -> list[list[int]]:
    """
    Strategy:
    Start with all zeros and then edit
    the lists one-by-one
    """

    """Start by making an empty list"""
    all_permu = []

    """Then make a list that contain n amount of 0's """
    all_zero = ["0"] * n

    """Calculate hvor many permutations of n there is"""
    amount_permu = 2**n

    """
    Start by going through the lists of 0's one-by-one
    until reaching the number of permutations
    """
    
    i = 0
    while i < amount_permu:
        
        """
        Python includes the bin() function returns the binary
        represenation of a given number. Unfortunately it has
        some atributes that are unwanted in this 
        specific use-case. 
        
        By default bin() returns a string with the prefix "0b".
        This can be avoided by either slicing the string using
        list comprehension and removing the two first 
        charactors. Alternatly can the inbuilt function
        format() be used which can convert numbers to multiple
        different repretations, including binary 
        without the "0b" prefix.

        Another attribute that both bin() and format() share
        is that they will write binary values with as few digits
        as possible by not including reduntant 0', i.e. 0's
        to the left of the first 1. For example if you are write
        bin(3) and bin(9) you get 0b11 and 0b1001 which contain
        different amounts of digit. This attribute is undesired 
        in this use case, since we don't want to count in binary
        but calculate all permutations of 0 and 1 which includes
        binary values that start with 0.

        This can be dealt with be using the inbuilt function
        zfill(), that can pad a string with the charactor "0" 
        n times at the beginning if a string.

        By combining format() and zfill() we can make the binary
        representation with a specific amount of digits.

        In this loop i is equel to the permutation we 
        want to write.

        Unfortunately since bin() and format() returns
        string so their output needs to be converted
        since we want lists of lists of integers.
        """
        #v = bin(i)[2:].zfill(n)
        v = format(i,"b").zfill(n)
        
        """
        Altough a bit overkill, by using map() we can convert
        the charactors in the output of format() function to
        int. The output of map() is converted to a list, since
        map() itself outputs a "map object" in Python.
        Then all the converted lists are appened to
        the list we return at the end of the function
        """
        all_permu.append(list(map(lambda x,y : int(x) | int(y),all_zero,v)))
        i = i +1

    return all_permu
