# Write Python statements to input two numbers and assign the smaller of the two to a varible called minimum

minimum = 0

num1 = input("Enter a number: ")
num2 = input("One more: ")

if num1 <= num2:
    minimum = num1
if num1 >= num2:
    minimum = num2
print(minimum)
