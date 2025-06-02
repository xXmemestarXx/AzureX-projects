# This script solves  if two numbers a and b are congruent modulo m.

print(f"This solves questions in the format a === b (mod m)")

def check_congruence(a, b, m):
    if a % m == b % m:
        print(f"{a} is congruent to {b} modulo {m}.")
    else:
        print(f"{a} is NOT congruent to {b} modulo {m}.")

# Get user input
a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter m (modulus): "))

check_congruence(a, b, m)
