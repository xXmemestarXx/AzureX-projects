# What would be the result of setting maxResult = 0,minResult = 100, testResult = 0 at the start of the program
#  And having just one input statement as the first statement in the loop?
# Alter the program to output "No results input" if -1 is input
testResult = int(input("Please enter test result: "))
maxResult = testResult
minResult = testResult
testResult = 0

while testResult != -1:
    if testResult > maxResult:
        maxResult = testResult
        if testResult < minResult:
            maxResult = testResult
    testResult = int(input("Please enter test result (To exit enter -1): "))

    if testResult == -1:
        print("Bye")

print("Max is: ", maxResult)
print("Min is: ", minResult)

