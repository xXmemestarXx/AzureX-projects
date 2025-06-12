from network_rev_5 import *
import comparator_rev_6 as Comp

print(f"")
print(f"------- test 1 start -------")
print(f"")
print(f"Testing to_string()")

Net = empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)
append(Com_1,Net)
append(Com_2,Net)

print(f"The network object to convert: {Net}")
print(f"Converted to string: {to_string(Net)}")

print(f"")
print(f"------- test 1 end -------")
print(f"")

print(f"")
print(f"------- test 2 start -------")
print(f"")
print(f"Testing empty_network()")
print(f"Test a empty network {empty_network()}")


print(f"")
print(f"------- test 2 end -------")
print(f"")

print(f"")
print(f"------- test 3 start -------")
print(f"")

Net = empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)

print(f"Testing append()")
print(f"Before append(): {Net}")
append(Com_1,Net)
append(Com_2,Net)
print(f"After append(): {Net}")

print(f"")
print(f"------- test 3 end -------")
print(f"")

print(f"")
print(f"------- test 4 start -------")
print(f"")

print(f"Testing size()")
Net = empty_network()
print(f"Before append, {Net}")
print(f"Before append, size: {size(Net)}")

Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)
append(Com_1,Net)
append(Com_2,Net)

print(f"After append, {Net}")
print(f"After append, size: {size(Net)}")

print(f"")
print(f"------- test 4 end -------")
print(f"")

print(f"")
print(f"------- test 5 start -------")
print(f"")

print(f"Testing max_channel()")  

Net = empty_network()
Com_1 = Comp.make_comparator(0,1)
append(Com_1,Net)
print(f"Network to test: {Net}")
print(f"Max channel: {max_channel(Net)}")

Com_2 = Comp.make_comparator(1,2)
Com_3 = Comp.make_comparator(3,4)

append(Com_2,Net)
append(Com_3,Net)

print(f"Network to test: {Net}")
print(f"Max channel: {max_channel(Net)}")

print(f"")
print(f"------- test 5 end -------")
print(f"")

print(f"")
print(f"------- test 6 start -------")
print(f"")

print(f"Testing is_standard()")  

Net = empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)
Com_3 = Comp.make_comparator(4,3)
append(Com_1,Net)
append(Com_2,Net)
append(Com_3,Net)

print(f"")
print(f"Network to test: {Net}")
print(f"Does the network only contain std comparators: {is_standard(Net)}")
print(f"")
Net_1 = empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(4,5)
Com_3 = Comp.make_comparator(2,5)
append(Com_1,Net_1)
append(Com_2,Net_1)
append(Com_3,Net_1)

print(f"Network to test: {Net_1}")
print(f"Does the network only contain std comparators: {is_standard(Net_1)}")

print(f"")
print(f"------- test 6 end -------")
print(f"")

print(f"")
print(f"------- test 7 start -------")
print(f"")

print(f"Testing apply()")

Net = empty_network()
Com_1 = Comp.make_comparator(1,2)
Com_2 = Comp.make_comparator(3,4)
Com_3 = Comp.make_comparator(0,1)


append(Com_1,Net)
append(Com_2,Net)
append(Com_3,Net)

v = [1,2,0,4,3]

print(f"Testing sorting the network with correct comparators")
print(f"")
print(f"{Net}")
print(f"")
print(f"List before: {v}")
print(f"")
print(f"Each step taken for sorting the list")
print(f"")
print(f"List after: {apply(Net,v)}")
print(f"")

Net_1 = empty_network()
Com_1 = Comp.make_comparator(1,3)
Com_2 = Comp.make_comparator(1,2)
Com_3 = Comp.make_comparator(3,4)
Com_4 = Comp.make_comparator(2,3)

append(Com_1,Net_1)
append(Com_2,Net_1)
append(Com_3,Net_1) 
append(Com_4,Net_1)

w = [1,2,0,4,3]

print(f"Testing sorting the network with wrong comparators")
print(f"")
print(f"{Net_1}")
print(f"")
print(f"List before: {w}")
print(f"")
print(f"List after: {apply(Net_1,w)}")

print(f"")
print(f"------- test 7 end -------")
print(f"")

print(f"")
print(f"------- test 8 start -------")
print(f"")

print(f"Testing outputs()")

Net = empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(0,2)
Com_3 = Comp.make_comparator(1,2)

append(Com_1,Net)
append(Com_2,Net)
append(Com_3,Net)

w = [[36,25,25],[36563236,63425,4433660]]
print(f"Testing sorting the network with correct comparators")
print(f"")
print(f"{Net}")
print(f"List before: {w}")
print(f"")
print(f"List after: {outputs(Net,w)}")
print(f"")

print(f"")
print(f"------- test 8 end -------")
print(f"")

print(f"")
print(f"------- test 9 start -------")
print(f"")

print(f"Testing all_outputs()")

Net = empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(0,2)
Com_3 = Comp.make_comparator(1,2)

append(Com_1,Net)
append(Com_2,Net)
append(Com_3,Net)

print(f"Network to test with: {Net}")
print(f"All permutations unsorted: {all_outputs_test(3)}")
print(f"All permutations sorted: {all_outputs(Net, 3)}")

print(f"")
print(f"------- test 9 end -------")
print(f"")

print(f"")
print(f"------- test 10 start -------")
print(f"")

print(f"Testing is_sorting()")

print(f"")
print(f"For us to check is_sorting(), we need to check the cases where,")
print(f"Evertyhing is OK, and then all the false cases possible, being")
print(f"len == 0, is_standard() == false, max_channel > size-1, all if statements is true,")
print(f"but one comparator is missing")
print(f"")

Net = empty_network()

Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)
Com_3 = Comp.make_comparator(0,2)
Com_4 = Comp.make_comparator(0,2)

append(Com_1,Net)
append(Com_2,Net)
append(Com_3,Net)
append(Com_4,Net)

print(f"First case where the three criteria are OK")
print(f"Max: {max_channel(Net)}")

print(f"The network contains: {to_string(Net)}")
print(f"")

print(f"Is the network able to sort a network of size {3}: {is_sorting(Net,3)}")

Net = empty_network()

print(f"")
print(f"Second case where the network is empty")
print(f"Max: 0")

print(f"The network contains: {to_string(Net)}")
print(f"")

print(f"Is the network able to sort a network of size {0}: {is_sorting(Net,0)}")

print(f"")
print(f"Third case where the network includes not standard comparators.")
print(f"A standard comparator being i < j and i != j")

Net = empty_network()

Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(2,1)
Com_3 = Comp.make_comparator(0,2)

append(Com_1,Net)
append(Com_2,Net)
append(Com_3,Net)


print(f"Max: {max_channel(Net)}")

print(f"The network contains: {to_string(Net)}")
print(f"")

print(f"Is the network able to sort a network of size {3}: {is_sorting(Net,3)}")

print(f"")
print(f"Fourth case where the network size is greater than the max_channel")

Net = empty_network()

Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(0,2)
Com_3 = Comp.make_comparator(1,3)

append(Com_1,Net)
append(Com_2,Net)
append(Com_3,Net)


print(f"Max: {max_channel(Net)}")

print(f"The network contains: {to_string(Net)}")
print(f"")

print(f"Is the network able to sort a network of size {4}: {is_sorting(Net,5)}")

print(f"")
print(f"Fifth case where the network is missing one singular comparator")

Net = empty_network()

Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)

append(Com_1,Net)
append(Com_2,Net)

print(f"Max: {max_channel(Net)}")

print(f"The network contains: {to_string(Net)}")
print(f"")

print(f"Is the network able to sort a network of size {3}: {is_sorting(Net,3)}")

print(f"")
print(f"------- test 10 end -------")
print(f"")