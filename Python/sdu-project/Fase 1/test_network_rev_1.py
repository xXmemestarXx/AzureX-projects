from network_rev_1 import *

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



# Not inplemented yet

# print(f"------- test 4 begin -------")

# Net_4 = empty_network()

# for i in range(5):
#     append(i,Net_4)
#     print(f"The max channel in Net_3 is: {max_channel(Net_4)}")
#     if type(size(Net_4)) == int:
#         print(f"max_channel() returns an int")
#     else:
#         print(f"max_channel() does not return an int")
#     print(f"")    
# print(f"------- test 4 end -------")
# print(f"")

