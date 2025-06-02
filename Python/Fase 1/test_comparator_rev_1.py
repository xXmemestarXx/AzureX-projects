from comparator_rev_1 import *

print(f"------- test 1 begin -------")
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
print(f"------- test 1 end -------")
print(f"")

print(f"------- test 2 begin -------")
comp = make_comparator(i = 0, j = 0)
w = [3,4,2,5]
print(f"Normal: [3,4,2,5] => {apply(comp, w)}")
v = [1,2,4,5]
print(f"Sorted: [1,2,4,5] => {apply(comp, v)}")
z = [1,3,4,4]
print(f"Dublicated Sorted: [1,3,4,4] => {apply(comp, z)}")
k = [2,1,1,3]
print(f"Dublicated: [2,1,1,3] => {apply(comp, k)}")
print(f"")
print(f"------- test 2 end -------")
print(f"")

