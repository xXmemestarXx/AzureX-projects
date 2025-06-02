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
        
        v = format(i,"b").zfill(n)
        
        all_permu.append(list(map(lambda x,y : int(x) | int(y),all_zero,v,)))
        i = i + 1

    return all_permu