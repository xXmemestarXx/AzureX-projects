
import network as Netw
import filter_new as Filt
import functools
"""
can i find out the optimal score for every size n and just cut every filter that gets less than the score.
"""

def prune(w: list[Filt.Filter], n: int) -> list[Filt.Filter]:
    """Removes some filters on n channels from w."""
    return cool_prune(w,n)

def how_sorted(v: list[int]) -> int:
    """
    Gives score to a filter for how well it sorts a list.
    Every list gets 1 for each two elements that are sorted, 
    a perfectly sorted list gets a score equal to it's length minus one.
    DOCTEST

    test_list=[3,6,2,4]
    >>> how_sorted(test_list)
    2

    """
    if(len(v)<=1):
        return 0
    elif(v[0] <= v[1]):
        return 1 + how_sorted(v[1:])
    else:
        return (-1) + how_sorted(v[1:])

def make_list(n: int) -> list[list[int]]:
    """
    Makes 5 lists,
    1st. reverse list: [n, n-1, n-2, n-3,....., 1]
    2nd. alternating half sorted w. duplicated zeros: [1, 0, 3, 0, 5,...., n]
    3rd. binary alternating list [0, 1, 0, 1,...., 0]
    4th. sorted list [0, 1, 2, 3, 4, 5,....., n]
    5th. reversed halved list [4, 3, 2, 1, 9, 8, 7, 6, 5] if n==9

    Returnes a list of these 5 lists.
    DOCTEST
    
    >>> make_list(3)
    [[3,2,1], [9,0,11], [0,1,0], [0,1,2], [1,3,2]]]

    """

    j = 0
    ret_list = [[],[],[],[],[]]
    for i in range(0,n):
        ret_list[0] = ret_list[0] + [n - i]  
        ret_list[3] = ret_list[3] + [i]
        if(i % 2 == 0):
            ret_list[1] = ret_list[1] + [n*n + i]
            ret_list[2] = ret_list[2] + [0]
        else:
            ret_list[1] = ret_list[1] + [0]
            ret_list[2] = ret_list[2] + [1]
        s=(n//2)
        if(i < s):
            ret_list[4] = ret_list[4] + [s-i]
        else:
            ret_list[4] = ret_list[4] + [n-j]
            j = j + 1
    return ret_list

def calc_score(f: Filt.Filter,n: int) -> int:
    """
    Calculates the total score of a filter by using apply() from network on each list,
    score is infalted for some lists using weigths.
    
    DOCTEST

    n = 3
    Comp_1 = Comp.make_comparator(0, 1)
    Comp_2 = Comp.make_comparator(1, 2)
    Filter = Filt.make_empty_filter(n)
    Filter=Filt.add(Comp_1,Filter)
    Filter=Filt.add(Comp_2,Filter)
    >>> calc_score(Filter,3)
    11.4

    """
    
    list_weigth=[1, 1.2, 1.5, 2]
    whole_list= make_list(n)
    pts_list1 = how_sorted(Netw.apply(Filt.net(f),whole_list[0])) * list_weigth[3]
    pts_list2 = how_sorted(Netw.apply(Filt.net(f),whole_list[1])) * list_weigth[0]
    pts_list3 = how_sorted(Netw.apply(Filt.net(f),whole_list[2])) * list_weigth[1]
    pts_list4 = how_sorted(Netw.apply(Filt.net(f),whole_list[3])) * list_weigth[0]
    pts_list5 = how_sorted(Netw.apply(Filt.net(f),whole_list[4])) * list_weigth[2]
    return ( pts_list1 + pts_list2 + pts_list5 + pts_list3 + pts_list4 + pts_list5 )

def cool_prune(w: list[Filt.Filter],n: int) -> list[Filt.Filter]:
    """
    Uses a point system to find out which filters will advance, 
    point system consists of using calc_score() to find the highest score of all the filters, 
    and only passsing the ones that are close to that high_score, how close is proportional to
    length of w, the larger the list of filters the higher percentage of filters will get pruned.

    DOCTEST
    To be continued...
    """

    score_list= list(map(lambda x: calc_score(x,n), w)) # creates list by using map and calc_score on w
    high_score= functools.reduce(lambda a,b: a if a>b else b,score_list) #finds the higest value in score_list

    returned_list=[]
    i=0
    score_prox=high_score-(50/len(w))
    while( i < (len(score_list))): # prunes w by matching scores for each filter with the score_list.
        if(score_list[i] < score_prox):
            i=i+1
        else:
            returned_list.append(w[i])
            i=i+1

    return returned_list