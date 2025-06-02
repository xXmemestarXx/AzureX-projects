# This script finds lcm (Least common multiple) for a given n and m (where n and m are integers)
import numpy as np

print("lcm(n, m)")
n = int(input("n = "))
m = int(input("m = "))

res = np.lcm(n, m)

print(res)
