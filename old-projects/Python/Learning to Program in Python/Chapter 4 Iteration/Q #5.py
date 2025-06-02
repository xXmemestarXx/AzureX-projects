#Use astring.find(item) to alternate the program

#Original
#eIndex = -1
#sentence = input("Please enter a sentence: ")
#for ePosition in range(len(sentence)):
    #if sentence(ePosition) == "e":
        #eIndex = ePosition
        #print("Index of first 'e' is ", eIndex)
        #break

#if eIndex == -1:
    #print("There is no 'e' in the sentence.")

eIndex = -1
sentence = input("Please enter a sentence: ")
for ePosition in range(len(sentence)):
    if sentence(ePosition) == "e":
        eIndex = ePosition
        print("Index of first 'e' is ", eIndex)
        break

if eIndex == -1:
    print("There is no 'e' in the sentence.")


