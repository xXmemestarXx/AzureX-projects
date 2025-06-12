"""
vector_prune_test.py

Written by Valdemar H8G03

DM574 Exam project
"""

"""
Importing 3rd party libaries
"""
from dataclasses import *
import functools as Func

"""
Importing our own and our lecturer's modules
"""
import comparator as Comp
import network as Netw
import filter as Filt
import generate_new as Gene
import prune as Prun
import make_sorted_outputs as MSOP
import vector_prune as VEPR

print(f"")
print(f"------- test vector_prune.py -------")
print(f"")
print(f"------- test 1 begin -------")
print(f"")
print(f"Testing add_vectors()")
print(f"")

v1 = [[0,0],[0,1],[1,0],[1,1]]
v2 = [[2,0],[2,1],[2,0],[2,1]]
v3 = [[0,2],[0,2],[1,2],[1,2]]

print(f"Vector v1   : {v1}")
print(f"Added v1    : {VEPR.add_vectors(v1)}")
print(f"")
print(f"Vector v2   : {v2}")
print(f"Added v2    : {VEPR.add_vectors(v2)}")
print(f"")
print(f"Vector v2   : {v3}")
print(f"Added v2    : {VEPR.add_vectors(v3)}")
print(f"")

print(f"------- test 1 end -------")
print(f"")

#_________________________________________________________________#

print(f"")
print(f"------- test 2 begin -------")
print(f"")
print(f"Testing make_comparison_vectors()")
print(f"")

n1 = 3
n2 = 4
n3 = 5

print(f"n1      : {n1}")
print(f"vector  : {VEPR.make_comparison_vector(n1)}")
print(f"")
print(f"n2      : {n2}")
print(f"vector  : {VEPR.make_comparison_vector(n2)}")
print(f"")
print(f"n3      : {n3}")
print(f"vector  : {VEPR.make_comparison_vector(n3)}")
print(f"")

print(f"------- test 2 end -------")
print(f"")

#_________________________________________________________________#

print(f"")
print(f"------- test 3 begin -------")
print(f"")
print(f"Testing filter_vectors()")
print(f"")

filt_test = Filt.make_empty_filter(5)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(1,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(2,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(3,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)

filt_test2 = Filt.make_empty_filter(5)
filt_test2 = Filt.add(Comp.make_comparator(0,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,2), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)

print(f"Filter 1    :   {filt_test}")
print(f"vector      :   {VEPR.filter_vector(filt_test)}")
print(f"")
print(f"Filter 2    :   {filt_test2}")
print(f"vector      :   {VEPR.filter_vector(filt_test2)}")
print(f"")

print(f"------- test 3 end -------")
print(f"")

#_________________________________________________________________#

print(f"")
print(f"------- test 4 begin -------")
print(f"")
print(f"Testing all_filter_vectors()")
print(f"")

filt_test = Filt.make_empty_filter(5)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(1,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(2,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(3,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)

filt_test2 = Filt.make_empty_filter(5)
filt_test2 = Filt.add(Comp.make_comparator(0,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,2), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)

filt_test3 = Filt.make_empty_filter(5)
filt_test3 = Filt.add(Comp.make_comparator(0,1), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(3,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,1), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(3,4), filt_test3)

f = [filt_test,filt_test2,filt_test3]

print(f"list of Filters :   {f}")
print(f"list of vectors :   {VEPR.all_filter_vectors(f)}")
print(f"")

print(f"------- test 4 end -------")
print(f"")

#_________________________________________________________________#

print(f"")
print(f"------- test 5 begin -------")
print(f"")
print(f"Testing sqr_eu_dist()")
print(f"")

filt_test2 = Filt.make_empty_filter(5)
filt_test2 = Filt.add(Comp.make_comparator(0,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,2), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)

fv = VEPR.filter_vector(filt_test2)
cv = VEPR.make_comparison_vector(5)

print(f"Filter Vector       :   {fv}")
print(f"")
print(f"Comparison Vector  :   {cv}")
print(f"")
print(f"Sqr Dist Between    :   {VEPR.sqr_eu_dist(cv,fv)}")
print(f"")
print(f"------- test 5 end -------")
print(f"")

#_________________________________________________________________#

print(f"")
print(f"------- test 6 begin -------")
print(f"")
print(f"Testing all_dist()")
print(f"")

n = 5

filt_test = Filt.make_empty_filter(n)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(1,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(2,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(3,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)

filt_test2 = Filt.make_empty_filter(n)
filt_test2 = Filt.add(Comp.make_comparator(0,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,2), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)

filt_test3 = Filt.make_empty_filter(n)
filt_test3 = Filt.add(Comp.make_comparator(0,1), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(3,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,1), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(3,4), filt_test3)

f = [filt_test,filt_test2,filt_test3]

#fv = VEPR.all_filter_vectors(f)

cv = VEPR.make_comparison_vector(n)

print(f"Filter Vectors          :   {f}")
print(f"")
print(f"Comparison Vector       :   {cv}")
print(f"")
print(f"All Sqr Dist Between    :   {VEPR.all_dis(cv,f)}")
print(f"")
print(f"------- test 6 end -------")
print(f"")

#_________________________________________________________________#


print(f"------- test 7 begin -------")
print(f"")
print(f"sort_dist_and_filt()")
print(f"")


n = 5

filt_test = Filt.make_empty_filter(n)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(1,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(2,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(3,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)

filt_test2 = Filt.make_empty_filter(n)
filt_test2 = Filt.add(Comp.make_comparator(0,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,2), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)

filt_test3 = Filt.make_empty_filter(n)
filt_test3 = Filt.add(Comp.make_comparator(0,1), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(3,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,1), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(3,4), filt_test3)

f = [filt_test,filt_test2,filt_test3]

cv = VEPR.make_comparison_vector(n)

ds = VEPR.all_dis(cv,f)


print(f"Filter Vectors          :   {f}")
print(f"")
print(f"Comparison Vector       :   {cv}")
print(f"")
print(f"All Sqr Dist Between    :   {VEPR.all_dis(cv,f)}")
print(f"")
print(f"Sorted                  :   {VEPR.sort_dist_and_filt(ds,f)}")

print(f"")
print(f"------- test 7 end -------")
print(f"")

#_________________________________________________________________#


print(f"------- test 8 begin -------")
print(f"")
print(f"vector_prune()")
print(f"")


n = 5

filt_test = Filt.make_empty_filter(n)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(1,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(2,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(3,4), filt_test)
filt_test = Filt.add(Comp.make_comparator(0,4), filt_test)

filt_test2 = Filt.make_empty_filter(n)
filt_test2 = Filt.add(Comp.make_comparator(0,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,2), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(1,4), filt_test2)
filt_test2 = Filt.add(Comp.make_comparator(2,3), filt_test2)

filt_test3 = Filt.make_empty_filter(n)
filt_test3 = Filt.add(Comp.make_comparator(0,1), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(3,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,1), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(0,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,2), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(1,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,3), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(2,4), filt_test3)
filt_test3 = Filt.add(Comp.make_comparator(3,4), filt_test3)

f = [filt_test,filt_test2,filt_test3]

cv = VEPR.make_comparison_vector(n)

ds = VEPR.all_dis(cv,f)


print(f"Filter Vectors          :   {f}")
print(f"")
print(f"Comparison Vector       :   {cv}")
print(f"")
print(f"All Sqr Dist Between    :   {VEPR.all_dis(cv,f)}")
print(f"")
print(f"Sorted                  :   {VEPR.vector_prune(n,f,2)}")

print(f"")
print(f"------- test 8 end -------")
print(f"")
