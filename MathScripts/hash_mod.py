def calculate_modulo():
    # Get the number of values from the user
    num_values = int(input("Enter the number of values: "))
    
    # Get the modulus value
    mod_value = int(input("Enter the modulus value: "))

    # Initialize an empty list to store the results
    results = []

    # Loop to get each value and calculate its modulo
    for i in range(num_values):
        number = int(input(f"Enter number {i+1}: "))
        result = number % mod_value
        results.append(result)

    # Display the results
    print("\nResults:")
    for i, res in enumerate(results, 1):
        print(f"Number {i} modulo {mod_value} = {res}")

# Call the function
calculate_modulo()