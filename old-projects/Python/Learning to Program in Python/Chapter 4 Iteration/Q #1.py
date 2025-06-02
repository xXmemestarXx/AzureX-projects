# Write python code to do the following:
# (a) Print the numbers 10 - 0 starting at 10. Then print "Lift-off".
#  Import the time module at the start of the program with the statement import time.
#  Include a time delay of 1 second before printing each number, using the statement time.sleep(1).
# (b) Ask the user to enter 5 numbers. Keep a running total and print the total and the average of the numbers

# (a)
import time

for number in range (1,11):
    time.sleep(1)
    print(number)
input("Press Enter to Lift-off: ")
print("lift-off")

# (b)

keep_going = input("Do you wish to continue press enter if not type exit: ")
if keep_going == "next":
    pass
print("Welcome")
input("You will need to type in 5 numbers (pls make them different) press enter to continue")
num1 = input("1): ")
num2 = input("2): ")
num3 = input("3): ")
num4 = input("4): ")
num5 = input("5): ")
for numbers in range (int(num1), 6):
    print("List : ", numbers)
# Adding them together
total = int(num1) + int(num2) + int(num3) + int(num4) + int(num5)
print("Total: ", total)
# Taking the average number from input
average = int(num1) + int(num2) + int(num3) + int(num4) + int(num5) / 5
print("Average: ", average)

# exit handler
if keep_going == "exit":
    print("Bye!")



