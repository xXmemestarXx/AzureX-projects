from network_rev_2 import *
import comparator_rev_1  as comparator_1
import comparator_2_rev_1  as comparator_2

print(f"------- test 1 begin -------")
Net_1 = empty_network()


if type(to_string(Net_1)) == str:
    """
    Checks whether to_string succesfully converted Network.network to a string
    """

    print(f"Net_1 = {to_string(Net_1)}")
    print("is a string")
 
print(f"")
print(f"------- test 1 end -------")
print(f"")


print(f"------- test 2 begin -------")
Net_2 = empty_network()
append(1,Net_2)
print(f"first append: {Net_2.network}")
append(2,Net_2)
print(f"second append: {Net_2.network}")
print(f"")
print(f"------- test 2 end -------")
print(f"")



print(f"------- test 3 begin -------")

Net_3 = empty_network()

print(f"The size of Net_3 is: {size(Net_3)}")
print(f"")  

for i in range(5):
    append(i,Net_3)
    print(f"The size of Net_3 is: {size(Net_3)}")
    if type(size(Net_3)) == int:
        print(f"size() returns an int")
    else:
        print(f"size() does not return an int")
    print(f"")    

print(f"------- test 3 end -------")
print(f"")


print(f"------- test 4.0 begin -------")

Net_4 = empty_network()
Com_1 = comparator_1.make_comparator(1,2)
Com_2 = comparator_1.make_comparator(3,-1)

append(Com_1,Net_4)
append(Com_2,Net_4)

print(f"Net 4 contains: {to_string(Net_4)}")
print(f"")

print(f"The Max of Net 4 is: {max_channel(Net_4)}")
print(f"")

print(f"------- test 4.0 end -------")
print(f"")


# print(f"------- test 4.1 begin -------")

# Net_4 = empty_network()
# Com_1 = comparator_1.make_comparator(7,-1)
# Com_2 = comparator_1.make_comparator(3,5)

# append(Com_1,Net_4)
# append(Com_2,Net_4)

# print(f"Net 4 contains: {to_string(Net_4)}")
# print(f"")

# print(f"The Max of Net 4 is: {max_channel(Net_4)}")
# print(f"")

# print(f"------- test 4.1 end -------")
# print(f"")


print(f"------- test 5.0 begin-------")

Net_5 = empty_network()
Com_3 = comparator_1.make_comparator(-7,1)
Com_4 = comparator_1.make_comparator(3,5)

append(Com_3,Net_5)
append(Com_4,Net_5)

print(f"Net 5 contains: {to_string(Net_5)}")
print(f"")

print(f"Does Net_5 only contain std. Comparators?: {is_standard(Net_5)}")
print(f"")

print(f"------- test 5.0 end -------")
print(f"")


# print(f"------- test 5.1 begin-------")

# Net_5 = empty_network()
# Com_3 = comparator_1.make_comparator(12,1)
# Com_4 = comparator_1.make_comparator(3,5)

# append(Com_3,Net_5)
# append(Com_4,Net_5)

# print(f"Net 5 contains: {to_string(Net_5)}")
# print(f"")

# print(f"Does Net_5 only contain std. Comparators?: {is_standard(Net_5)}")
# print(f"")

# print(f"------- test 5.1 end -------")
# print(f"")