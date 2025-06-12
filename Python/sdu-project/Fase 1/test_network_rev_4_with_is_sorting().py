import network_rev_5 as Netw
import comparator_rev_6  as Comp

print(f"------- test 1 begin -------")
Net_1 = Netw.empty_network()

"""
Checks whether to_string succesfully converted Network.network to a string
"""

print(f"Net_1 = {Netw.to_string(Net_1)}")
print(f"Output is a {type(Netw.to_string(Net_1))}")
 
print(f"")
print(f"------- test 1 end -------")
print(f"")


print(f"------- test 2 begin -------")
Net_2 = Netw.empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,0)

Netw.append(Com_1,Net_2)
print(f"first append: {Net_2.network}")

Netw.append(Com_2,Net_2)
print(f"second append: {Net_2.network}")

print(f"")
print(f"------- test 2 end -------")
print(f"")



print(f"------- test 3 begin -------")

Net_3 = Netw.empty_network()

print(f"The size of Net_3 is: {Netw.size(Net_3)}")
print(f"")  

for i in range(5):
    Com = Comp.make_comparator(i,(i+1))
    
    Netw.append(Com,Net_3)
    
    print(f"The size of Net_3 is: {Netw.size(Net_3)}")
    
    print((f"size() outputs: {type(Netw.size(Net_3))}"))
    
    print(f"")    

print(f"------- test 3 end -------")
print(f"")


print(f"------- test 8.0 begin -------")

Net_4 = Netw.empty_network()

Com_3 = Comp.make_comparator(0,1)
Com_4 = Comp.make_comparator(1,2)
Com_5 = Comp.make_comparator(0,2)

Netw.append(Com_3,Net_4)
Netw.append(Com_4,Net_4)
Netw.append(Com_5,Net_4)

v = [[36,25,25],[36563236,63425,4433660]]

print(f"Net 4 contains: {Netw.to_string(Net_4)}")
print(f"")

print(f"List v contains before sorting: {v}")
print(f"")

print(f"List v contains after sorting: {Netw.outputs(Net_4,v)}")
print(f"")

print(f"------- test 8.0 end -------")
print(f"")

print(f"------- test 9.0 begin -------")

Net_5 = Netw.empty_network()
Com_6 = Comp.make_comparator(0,1)
Com_7 = Comp.make_comparator(1,2)
Com_8 = Comp.make_comparator(0,2)

Netw.append(Com_6,Net_5)
Netw.append(Com_7,Net_5)
Netw.append(Com_8,Net_5)



#v = [[36,25,25],[36563236,63425,4433660]]

print(f"Net 5 contains: {Netw.to_string(Net_5)}")
print(f"")

print(f"all sorted permutations of 0 and 1 of {3} length are: \n {Netw.all_outputs(Net_5,3)}")

#print(f"after sorting of {3} length: \n {Netw.outputs(Net_5,Netw.all_outputs(Net_5,3))}")

# for i in range(1,3):

#     print(f"length n is equel to: {i}")
#     print(f"")



#     print(f"all sorted permutations of 0 and 1 of {i} length are: n/ {Netw.all_outputs(Net_5,i)}")
#     print(f"")


print(f"------- test 9.0 end -------")
print(f"")


print(f"------- test 10.0 begin -------")

Net_6 = Netw.empty_network()

Com_9 = Comp.make_comparator(0,1)
Com_10 = Comp.make_comparator(1,2)
Com_11 = Comp.make_comparator(0,2)
Com_12 = Comp.make_comparator(0,2)

Netw.append(Com_9,Net_6)
Netw.append(Com_10,Net_6)
Netw.append(Com_11,Net_6)
Netw.append(Com_12,Net_6)


print(f"max : {Netw.max_channel(Net_6)}")

#v = [[36,25,25],[36563236,63425,4433660]]

print(f"Net 6 contains: {Netw.to_string(Net_6)}")
print(f"")

print(f"Is Net_6 able to sort a net of size {2}:\n {Netw.is_sorting(Net_6,3)}")

# for i in range(1,3):

#     print(f"length n is equel to: {i}")
#     print(f"")



#     print(f"all sorted permutations of 0 and 1 of {i} length are: n/ {Netw.all_outputs(Net_5,i)}")
#     print(f"")


print(f"------- test 10.0 end -------")
print(f"")


