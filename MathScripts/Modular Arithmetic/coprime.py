# This script checks if a and b are coprime
import math

def check_coprime(a, b) -> int:
    return math.gcd(a, b)

print(f"Check if a and b are coprime, by using the gcd(a,b) = 1")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if (check_coprime(a, b) == 1):
    print(f"{a} and {b} is coprime")
else: 
    print(f"{a} and {b} are not coprime")
