# This scipt checks if a list of numbers are a multipliatve inverse of x 

def is_multiplicative_inverse(a, m):
    # Check if a * x ≡ 1 (mod 10)
    x = 9
    return (a * x) % m == 1

# List of numbers to check
numbers_to_check = [1, 2, 9, 10, 17, 19, 23]
modulus = 10
multiplicative_inverses = []

# Check each number
for number in numbers_to_check:
    if is_multiplicative_inverse(number, modulus):
        multiplicative_inverses.append(number)

print("Multiplicative inverses of 9 modulo 10:", multiplicative_inverses)
