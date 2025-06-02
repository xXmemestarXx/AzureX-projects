from comparator_rev_4 import *

print(f"------- test 1 begin -------")
print(f"")
print(f"Testing make_comparator()")
print(f"")
i = 0
j = 2
c = make_comparator(i, j)
print(f"i = 0, j = 2 => {c}")

print(f"")
print(f"------- test 1 end -------")
print(f"")

print(f"------- test 2 begin -------")
print(f"")
print(f"Testing min_channel() & max_channel()")
print(f"")
i = 0
j = 2
c = make_comparator(i, j)
print(f"{c} => min = {min_channel(c)}, max = {max_channel(c)}")

print(f"")
print(f"------- test 2 end -------")
print(f"")

print(f"------- test 3 begin -------")
print(f"")
print(f"Testing is_standard()")
print(f"")
i = 0
j = 2
c = make_comparator(i, j)
print(f"i = {i} and j = {j} => {is_standard(c)}")
i = 2
j = 0
c = make_comparator(i, j)
print(f"i = {i} and j = {j} => {is_standard(c)}")
i = 2
j = 2
c = make_comparator(i, j)
print(f"i = {i} and j = {j} => {is_standard(c)}")

print(f"")
print(f"------- test 3 end -------")
print(f"")

print(f"------- test 4 begin -------")
print(f"")
print(f"Testing apply()")
print(f"")
comp = make_comparator(i = 0, j = 0)
w = [3,4,2,5]
print(f"Normal: [3,4,2,5] => {apply(comp, w)}")
v = [1,2,4,5]
print(f"Sorted: [1,2,4,5] => {apply(comp, v)}")
z = [1,3,4,4]
print(f"Duplicated Sorted: [1,3,4,4] => {apply(comp, z)}")
k = [2,1,1,3]
print(f"Duplicated: [2,1,1,3] => {apply(comp, k)}")
print(f"")
print(f"------- test 4 end -------")
print(f"")

print(f"------- test 5 begin -------")
print(f"")
print(f"Testing all_comparators()")
print(f"")
n = 3
print(f"n = 3 => {all_comparators(n)}")
n = 0
print(f"n = 0 => {all_comparators(n)}")
n = -3
print(f"n = -3 => {all_comparators(n)}")
print(f"")
print(f"------- test 5 end -------")
print(f"")

print(f"------- test 6 begin -------")
print(f"")
print(f"Testing std_comparators()")
print(f"")
n = 3
print(f"n = 3 => {std_comparators(n)}")
n = 0
print(f"n = 0 => {std_comparators(n)}")
n = -3
print(f"n = -3 => {std_comparators(n)}")
print(f"")
print(f"------- test 6 end -------")
print(f"")

print(f"------- test 7 begin -------")
print(f"")
print(f"Testing to_program()")
print(f"")
i = "i"
j = "j"
to_program_c = make_comparator(i = str(i), j = str(j))
print(to_program(Comparator(i, j), var = "network", aux = "temp"))
print(f"")
print(f"------- test 7 end -------")
