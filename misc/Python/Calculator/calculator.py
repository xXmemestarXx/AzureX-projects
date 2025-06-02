import mymath as m # Importing own module, with calc function

"""
Grabs user input and calls function from module with given input.
"""

a = int(input("Give me a number: "))
b = int(input("One more: "))
c = int(input("Give me a number, 1 = sub, 2 = add, 3 = mul, 4 = div, 5 = divdiv: "))
m.calc(a, b, c)
