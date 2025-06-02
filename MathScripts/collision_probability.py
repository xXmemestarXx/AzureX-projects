import math

def collision_probability(n, k):
    # Hvis n er større end k, er sandsynligheden 0, da k ikke kan rumme n elementer uden kollision.
    if n > k:
        return 0
    
    # Beregning af sandsynligheden for ingen kollisioner
    no_collision_prob = 1.0
    for i in range(n):
        no_collision_prob *= (k - i) / k
    
    return no_collision_prob

def main():
    # Input fra brugeren
    n = int(input("Indtast antallet af elementer (n): "))
    k = int(input("Indtast antallet af pladser (k): "))
    
    # Beregning af sandsynlighed
    prob = collision_probability(n, k)
    prob_calc = prob * 100
    prob_calc_2 = 100 - prob_calc
    
    # Vis resultatet
    print(f"Sandsynligheden for ingen kollisioner er: {prob_calc:.2f}")
    print(f"Sandsynligheden for kollison er: {prob_calc_2:.2f}")
    
# Kør programmet
main()
