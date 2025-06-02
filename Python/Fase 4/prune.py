import filter_new as Filt
import functools
import network as Netw

def prune(w:list[Filt.Filter], n: int) -> list[Filt.Filter]:
    """Returns the implementation of prune used, change the function to either
      'boring_prune', 'score_prune' or 'vector_prune.' to use different implementations."""
    return vector_prune(w, n)

    
def boring_prune(w, n):
    """
    Returns all filters with unique outputs from input list w.
    Implementation is based on the sieve of Eratosthenes algorithm.
    Using a boolean list and two for-each-loops, the function looks
    through the given list and compare the outputs for the filters,
    where it crosses out filters if the outputs are non-unique

    reg:
    len(w) > 0   
    """

    keep = [True for i in range(0, len(w)+1)]
    pruned = []

    for i in range(0,len(w)):
        if keep[i]:
            pruned.append(w[i])
            for j in range(i,len(w)):
                if Filt.out(w[i]) == Filt.out(w[j]):
                    keep[j] = False
    return pruned

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
        return how_sorted(v[1:])

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
    [[3,2,1], [1,0,3], [0,1,0], [0,1,2], [1,3,2]]]

    """

    ret_list = [[],[],[],[],[]]
    ret_list[0] = list(range(n,0,-1))
    ret_list[1] = list(map(lambda x: x if x%2!=0 else 0, range(1,n+1)))
    ret_list[2] = list(map(lambda x: 1 if x%2==0 else 0, range(1,n+1)))
    ret_list[3] = list(range(n))
    ret_list[4] = list(list(range(n//2,0,-1)) + list(range(n,n//2,-1)))
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
    14.4

    """
    
    list_weigth=[1, 1.2, 1.5, 2]
    whole_list= make_list(n)
    pts_list1 = how_sorted(Netw.apply(Filt.net(f),whole_list[0])) * list_weigth[3]
    pts_list2 = how_sorted(Netw.apply(Filt.net(f),whole_list[1])) * list_weigth[0]
    pts_list3 = how_sorted(Netw.apply(Filt.net(f),whole_list[2])) * list_weigth[1]
    pts_list4 = how_sorted(Netw.apply(Filt.net(f),whole_list[3])) * list_weigth[0]
    pts_list5 = how_sorted(Netw.apply(Filt.net(f),whole_list[4])) * list_weigth[2]
    return ( pts_list1 + pts_list2 + pts_list5 + pts_list3 + pts_list4 + pts_list5 )

def score_prune(w: list[Filt.Filter],n: int) -> list[Filt.Filter]:
    """
    Uses a point system to find out which filters will advance, 
    point system consists of using calc_score() to find the
    highest score of all the filters, and only passsing the
    ones that are close to that high_score, 
    how close it is proportional to
    length of w, the larger the list of filters the higher percentage
    of filters will get pruned.
    """

    # creates list by using map and calc_score on w
    score_list= list(map(lambda x: calc_score(x,n), w)) 
    # finds the higest value in score_list
    high_score= functools.reduce(lambda a,b: a if a>b else b,score_list) 

    returned_list=[]
    i=0
    score_prox=high_score-(50/len(w))
    # prunes w by matching scores for each filter with the score_list.
    while( i < (len(score_list))): 
        if(score_list[i] < score_prox):
            i=i+1
        else:
            returned_list.append(w[i])
            i=i+1

    return returned_list

def add_vectors(v: list[list[int]]) -> list[int]:
    """
    Adds all the vectors in v and returns a single vector

    reg:
    all vectors need to be the same length

    len(v) > 0
    """
    new_v = [0 for x in range(0,len(v[0]))]
    
    i = 0

    while i < len(v):
        j = 0

        while j < len(v[0]):
            new_v[j] = new_v[j] + v[i][j]
            j = j + 1
        
        i = i + 1
        
    return new_v

def make_comparison_vector(n: int) -> list[int]:
    """
    Quickly makes the vector that would result
    from adding all the vectors in the
    outputs of a sorting network for n channels
    
    reg:
    n > 0
    """
    res = []
    for i in range(1,n+1):
        res.append(i)
    return res

def filter_vector(f: Filt.Filter):
    """
    Takes a Filters outputs and returns a 
    new vector.

    DOCTEST
    Filt.out(Filter)=  [[0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0],
                        [1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 1],
                        [1, 0, 0, 1, 1],
                        [0, 0, 1, 1, 1],
                        [1, 0, 1, 1, 1],
                        [0, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1]]
    >>> filter_vector(Filter)
    [4, 2, 4, 8, 7]          
    """
    return add_vectors(Filt.out(f))

def sqr_eu_dist(cv: list,v: list) -> int:
    """
    Calculates the square distance between two
    vector using Pythagoras' theorem
    """
    return sum(list(map(lambda x,y: (x-y)**2,cv,v)))

def all_dis(cv: list[int],fv: list[Filt.Filter]) -> list[int]: 
    """
    Calculates distances between a constant vector and
    all the vectors generated from a list of Filters
    
    DOCTEST

    filt_test = Filt.make_empty_filter(5)
    filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)
    filt_test = Filt.add(Comp.make_comparator(1,4), filt_test)
    
    filt_test2 = Filt.make_empty_filter(5)
    filt_test2 = Filt.add(Comp.make_comparator(2,4), filt_test2)
    filt_test2 = Filt.add(Comp.make_comparator(1,4), filt_test2)
    filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)

    fv = [filt_test,filt_test2]
    cv = make_comparison_vector(5)
    
    >>> all_dis(cv,fv)
    [291, 151]
    """
    all_distances = []
    for i in range(0,len(fv)):
        all_distances.append(sqr_eu_dist(cv,filter_vector(fv[i])))
    return all_distances

def sort_dist_and_filt(v: list[int],w: list[Filt.Filter]) -> list[Filt.Filter]:
    """
    Bubble sorts the Filter according to their distances from the
    comparison vector. Their distances is in another list
    and not part of the Filter data structures themselves,
    therefore two lists are required.

    The main difference from bubble sort is that we sort two lists

    req:
    len(v) = len(w) 
    len(v), len(w) > 0

    DOCTEST

    v = [1,5,8,3]
    w = [Filter_1,Filter_2,Filter_3,Filter_4]

    >>> sort_dist_and_filt(v,w)
    [Filter_1,Filter_4,Filter_2,Filter_3]
    """
    dis = v[0:] #to avoid changing input list
    fil = w[0:] #to avoid changing input list

    for i in range(0,len(fil)): #v and w should be equally long
        for j in range(0,(len(fil)-1)-i):
            if dis[j] > dis[j+1]:
                dis[j], dis[j+1] = dis[j+1], dis[j]
                fil[j], fil[j+1] = fil[j+1], fil[j]
    return fil

def vector_prune(w: list[Filt.Filter], n: int):
    """
    Makes vector from the outputs in the list of Filter,
    whereafter the function calculates the distances between 
    the vectors and a constant vector created from a sorting 
    networks outputs. 

    Then sortes the Filters according to their distances from 
    the comparison vector and returns the first fraction of them
    determined by the denominator
    """
    cov = make_comparison_vector(n)

    dis = all_dis(cov,w)
    
    pru = sort_dist_and_filt(dis,w)

    # Slices the list invers proportionally, so we keep fewer
    # Filters the longer the list of Filter gets
    return pru[0: int(1/(len(pru))*100000)]