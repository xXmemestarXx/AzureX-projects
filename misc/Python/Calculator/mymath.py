def calc(a, b, c):
    """
    This function looks at a given integer and uses it to make a choice in operation.
    Then prints the given operations output.
    If c does not match a given value it returns "Error"
    """
    if c == 1:
        sub = a - b
        print(sub)
    if c == 2: 
        add = a + b
        print(add)
    if c == 3:
        mul = a * b
        print(mul)
    if c == 4:
        div = int(a / b)
        print(div)
    if c == 5:
        divdiv = a // b
        print(divdiv)
    else: 
        return "Error"

   