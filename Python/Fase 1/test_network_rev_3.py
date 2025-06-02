from network_rev_3 import *
import comparator_rev_3  as Comp

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
Com_1 = Comp.make_comparator(1,2)
Com_2 = Comp.make_comparator(3,-1)

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
Com_3 = Comp.make_comparator(-7,1)
Com_4 = Comp.make_comparator(3,5)

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


print(f"------- test 6.0 begin-------")

Net_6 = empty_network()
Com_5 = Comp.make_comparator(-7,19)
Com_6 = Comp.make_comparator(3,-5)
Com_7 = Comp.make_comparator(3,42)

w = [1,4,7,4,767,8,5,654,454,6,8,5,43,43,315563]
#w = [[1,6],[32,7],[42,4,-2,5,7,22,5],[32343,42,74]]

append(Com_5,Net_6)
append(Com_6,Net_6)
append(Com_7,Net_6)

print(f"Net 6 contains: {to_string(Net_6)}")
print(f"")

print(f"List w contains before: {w}")
print(f"")

print(f"List w contains after: {apply(Net_6,w)}")
print(f"")

print(f"------- test 6.0 end -------")
print(f"")


print(f"------- test 7.0 begin-------")

Net_7 = empty_network()
Com_8 = Comp.make_comparator(-7,19)
Com_9 = Comp.make_comparator(3,-5)
Com_10 = Comp.make_comparator(3,42)

u = [[1,6],[32,7],[42,4,-2,5,7,22,5],[32343,42,74]]

append(Com_8,Net_7)
append(Com_9,Net_7)
append(Com_10,Net_7)

print(f"Net 7 contains: {to_string(Net_7)}")
print(f"")

print(f"List u contains before: {u}")
print(f"")

print(f"List u contains after: {outputs(Net_7,u)}")
print(f"")

print(f"------- test 7.0 end -------")
print(f"")
