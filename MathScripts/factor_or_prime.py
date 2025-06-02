# Based on Theorem N composite => N has a prime divisor <= \sqrt(N)
# This script is checking if a number N is prime or has a factor up to \sqrt(N)
import math
n = int(input("n: "))

def factor(n):
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            return f"Divisor {x}"
    return "Prime"
print(factor(n))