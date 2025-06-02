# This script uses the CRT (Chinese Remainder Theorem) to find all solutions to a system of congruences.
# a_i and n_i format is x === a_i mod n_i.
# The soultion is given as x === a mod n => x = a + m * k, where k is any integer.
# Inspired by Exercise Sheet 15 Section 4.4 Exercise 20

from functools import reduce

def extended_gcd(a, b):
    """
    Computes the extended GCD of a and b.
    Returns (g, x, y) where g is gcd(a, b) and x, y satisfy the equation: ax + by = g.
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def chinese_remainder_theorem(congruences):
    """
    Solves a system of congruences using the Chinese Remainder Theorem.
    
    Arguments:
        congruences: A list of tuples (a_i, n_i), where x \u2261 a_i (mod n_i).

    Returns:
        A tuple (x, N), where x is the solution modulo N, and N is the product of moduli.
        If the moduli are not coprime, raises a ValueError.
    """
    def combine_congruences(c1, c2):
        a1, n1 = c1
        a2, n2 = c2

        g, m1, m2 = extended_gcd(n1, n2)
        if (a1 - a2) % g != 0:
            raise ValueError("No solution exists for the given system of congruences.")

        # Combine into a single congruence
        lcm = n1 * (n2 // g)  # Least common multiple
        x = (a1 * m2 * (n2 // g) + a2 * m1 * (n1 // g)) % lcm
        return x, lcm

    x, N = reduce(combine_congruences, congruences)
    return x % N, N

# Example Usage
if __name__ == "__main__":
    try:
        print("Enter the number of congruences:")
        num_congruences = int(input().strip())
        congruences = []

        for i in range(num_congruences):
            print(f"Enter a_i and n_i for congruence {i + 1} (separated by a space):")
            a_i, n_i = map(int, input().strip().split())
            congruences.append((a_i, n_i))

        solution, modulus = chinese_remainder_theorem(congruences)
        print(f"A solution to the system is x = {solution} (mod {modulus}).")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)
