# WHat would be the result of setting maxResult = 0,minResult = 100, testResult = 0 at the start of the program
#  And having just one input statement as the first statement in the loop?
maxResult = 0
minResult = 100
testResult = 0

while testResult != -1:
    testResult = int(input("Please enter test result: " "(Enter -1 to exit): "))

print("Max is: ", maxResult)
print("Min is: ", minResult)

print("Enter -1 to exit")
