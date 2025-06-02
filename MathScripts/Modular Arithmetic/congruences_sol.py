# This scipt solves congruences systems, where the question is finding what system has a solution between a and b.
# A system being x = a mod m, x = a_1 mod m_1, x = a_2 mod m_2
def has_solution(r, m, a, b):
    # Reduce r modulo m
    r %= m

    # Find the smallest x >= a
    k = (a - r + m - 1) // m  # Ceiling division
    x = r + k * m

    # Check if x <= b
    return x <= b

def main():
    # Get inputs from the user
    print("Solve x ≡ r (mod m) in the range [a, b].")
    r = int(input("Enter r (remainder): "))
    m = int(input("Enter m (modulus): "))
    a = int(input("Enter a (lower bound): "))
    b = int(input("Enter b (upper bound): "))

    # Check if a solution exists
    if has_solution(r, m, a, b):
        print(f"A solution exists for x ≡ {r} (mod {m}) in the range [{a}, {b}].")
    else:
        print(f"No solution exists for x ≡ {r} (mod {m}) in the range [{a}, {b}].")

if __name__ == "__main__":
    main()
