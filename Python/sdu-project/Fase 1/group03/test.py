import network as Netw
import comparator as Comp

print(f"")
print(f"------- test comparator.py -------")
print(f"")
print(f"------- test 1 begin -------")
print(f"")
print(f"Testing make_comparator()")
print(f"")
i = 0
j = 2
c = Comp.make_comparator(i, j)
print(f"i = 0, j = 2 => {c}")

print(f"")
print(f"------- test 1 end -------")
print(f"")

print(f"------- test 2 begin -------")
print(f"")
print(f"Testing min_channel() & max_channel()")
print(f"")
i = 0
j = 2
c = Comp.make_comparator(i, j)
print(f"{c} => min = {Comp.min_channel(c)}, max = {Comp.max_channel(c)}")

print(f"")
print(f"------- test 2 end -------")
print(f"")

print(f"------- test 3 begin -------")
print(f"")
print(f"Testing is_standard()")
print(f"")
i = 0
j = 2
c = Comp.make_comparator(i, j)
print(f"i = {i} and j = {j} => {Comp.is_standard(c)}")
i = 2
j = 0
c = Comp.make_comparator(i, j)
print(f"i = {i} and j = {j} => {Comp.is_standard(c)}")
i = 2
j = 2
c = Comp.make_comparator(i, j)
print(f"i = {i} and j = {j} => {Comp.is_standard(c)}")

print(f"")
print(f"------- test 3 end -------")
print(f"")

print(f"------- test 4 begin -------")
print(f"")
print(f"Testing apply()")
print(f"")
comp = Comp.make_comparator(i = 0, j = 0)
w = [3,4,2,5]
print(f"Normal: [3,4,2,5] => {Comp.apply(comp, w)}")
v = [1,2,4,5]
print(f"Sorted: [1,2,4,5] => {Comp.apply(comp, v)}")
z = [1,3,4,4]
print(f"Duplicated Sorted: [1,3,4,4] => {Comp.apply(comp, z)}")
k = [2,1,1,3]
print(f"Duplicated: [2,1,1,3] => {Comp.apply(comp, k)}")
print(f"")
print(f"------- test 4 end -------")
print(f"")

print(f"------- test 5 begin -------")
print(f"")
print(f"Testing all_comparators()")
print(f"")
n = 3
print(f"n = 3 => {Comp.all_comparators(n)}")
n = 0
print(f"n = 0 => {Comp.all_comparators(n)}")
n = -3
print(f"n = -3 => {Comp.all_comparators(n)}")
print(f"")
print(f"------- test 5 end -------")
print(f"")

print(f"------- test 6 begin -------")
print(f"")
print(f"Testing std_comparators()")
print(f"")
n = 3
print(f"n = 3 => {Comp.std_comparators(n)}")
n = 0
print(f"n = 0 => {Comp.std_comparators(n)}")
n = -3
print(f"n = -3 => {Comp.std_comparators(n)}")
print(f"")
print(f"------- test 6 end -------")
print(f"")

print(f"------- test 7 begin -------")
print(f"")
print(f"Testing to_program()")
print(f"")
i = "i"
j = "j"
to_program_c = Comp.make_comparator(i = str(i), j = str(j))
print(Comp.to_program(Comp.Comparator(i, j), var = "network", aux = "temp"))
print(f"")
print(f"------- test 7 end -------")

print(f"")
print(f"------- test network.py -------")
print(f"")
print(f"------- test 1 start -------")
print(f"")
print(f"Testing to_string()")

Net = Netw.empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)
Netw.append(Com_1,Net)
Netw.append(Com_2,Net)

print(f"The network object to convert: {Net}")
print(f"Converted to string: {Netw.to_string(Net)}")

print(f"")
print(f"------- test 1 end -------")
print(f"")

print(f"")
print(f"------- test 2 start -------")
print(f"")
print(f"Testing empty_network()")
print(f"Test a empty network {Netw.empty_network()}")


print(f"")
print(f"------- test 2 end -------")
print(f"")

print(f"")
print(f"------- test 3 start -------")
print(f"")

Net = Netw.empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)

print(f"Testing append()")
print(f"Before append(): {Net}")
Netw.append(Com_1,Net)
Netw.append(Com_2,Net)
print(f"After append(): {Net}")

print(f"")
print(f"------- test 3 end -------")
print(f"")

print(f"")
print(f"------- test 4 start -------")
print(f"")

print(f"Testing size()")
Net = Netw.empty_network()
print(f"Before append, {Net}")
print(f"Before append, size: {Netw.size(Net)}")

Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)
Netw.append(Com_1,Net)
Netw.append(Com_2,Net)

print(f"After append, {Net}")
print(f"After append, size: {Netw.size(Net)}")

print(f"")
print(f"------- test 4 end -------")
print(f"")

print(f"")
print(f"------- test 5 start -------")
print(f"")

print(f"Testing max_channel()")  

Net = Netw.empty_network()
Com_1 = Comp.make_comparator(0,1)
Netw.append(Com_1,Net)
print(f"Network to test: {Net}")
print(f"Max channel: {Netw.max_channel(Net)}")

Com_2 = Comp.make_comparator(1,2)
Com_3 = Comp.make_comparator(3,4)

Netw.append(Com_2,Net)
Netw.append(Com_3,Net)

print(f"Network to test: {Net}")
print(f"Max channel: {Netw.max_channel(Net)}")

print(f"")
print(f"------- test 5 end -------")
print(f"")

print(f"")
print(f"------- test 6 start -------")
print(f"")

print(f"Testing is_standard()")  

Net = Netw.empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)
Com_3 = Comp.make_comparator(4,3)
Netw.append(Com_1,Net)
Netw.append(Com_2,Net)
Netw.append(Com_3,Net)

print(f"")
print(f"Network to test: {Net}")
print(f"Does the network only contain std comparators: {Netw.is_standard(Net)}")
print(f"")
Net_1 = Netw.empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(4,5)
Com_3 = Comp.make_comparator(2,5)
Netw.append(Com_1,Net_1)
Netw.append(Com_2,Net_1)
Netw.append(Com_3,Net_1)

print(f"Network to test: {Net_1}")
print(f"Does the network only contain std comparators: {Netw.is_standard(Net_1)}")

print(f"")
print(f"------- test 6 end -------")
print(f"")

print(f"")
print(f"------- test 7 start -------")
print(f"")

print(f"Testing apply()")

Net = Netw.empty_network()
Com_1 = Comp.make_comparator(1,2)
Com_2 = Comp.make_comparator(3,4)
Com_3 = Comp.make_comparator(0,1)


Netw.append(Com_1,Net)
Netw.append(Com_2,Net)
Netw.append(Com_3,Net)

v = [1,2,0,4,3]

print(f"Testing sorting the network with correct comparators")
print(f"")
print(f"{Net}")
print(f"")
print(f"List before: {v}")
print(f"")
print(f"Each step taken for sorting the list")
print(f"")
print(f"List after: {Netw.apply(Net,v)}")
print(f"")

Net_1 = Netw.empty_network()
Com_1 = Comp.make_comparator(1,3)
Com_2 = Comp.make_comparator(1,2)
Com_3 = Comp.make_comparator(3,4)
Com_4 = Comp.make_comparator(2,3)

Netw.append(Com_1,Net_1)
Netw.append(Com_2,Net_1)
Netw.append(Com_3,Net_1) 
Netw.append(Com_4,Net_1)

w = [1,2,0,4,3]

print(f"Testing sorting the network with wrong comparators")
print(f"")
print(f"{Net_1}")
print(f"")
print(f"List before: {w}")
print(f"")
print(f"List after: {Netw.apply(Net_1,w)}")

print(f"")
print(f"------- test 7 end -------")
print(f"")

print(f"")
print(f"------- test 8 start -------")
print(f"")

print(f"Testing outputs()")

Net = Netw.empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(0,2)
Com_3 = Comp.make_comparator(1,2)

Netw.append(Com_1,Net)
Netw.append(Com_2,Net)
Netw.append(Com_3,Net)

w = [[36,25,25],[36563236,63425,4433660]]
print(f"Testing sorting the network with correct comparators")
print(f"")
print(f"{Net}")
print(f"List before: {w}")
print(f"")
print(f"List after: {Netw.outputs(Net,w)}")
print(f"")

print(f"")
print(f"------- test 8 end -------")
print(f"")

print(f"")
print(f"------- test 9 start -------")
print(f"")

print(f"Testing all_outputs()")

Net = Netw.empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(0,2)
Com_3 = Comp.make_comparator(1,2)

Netw.append(Com_1,Net)
Netw.append(Com_2,Net)
Netw.append(Com_3,Net)

print(f"Network to test with: {Net}")
print(f"All permutations unsorted: {Netw.permutations(3)}")
print(f"All permutations sorted: {Netw.all_outputs(Net, 3)}")

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
print(f"len == 0, max_channel != size-1, all if statements is true,")
print(f"but one comparator is missing")
print(f"")

Net = Netw.empty_network()

com1 = Comp.make_comparator(0,1)
com2 = Comp.make_comparator(0,2)
com3 = Comp.make_comparator(1,2)

Netw.append(com1,Net)
Netw.append(com2,Net)
Netw.append(com3,Net)

print(f"First case where the three criteria are OK")
print(f"Max: {Netw.max_channel(Net)}")

print(f"The network contains: {Netw.to_string(Net)}")
print(f"")

print(f"Is the network able to sort a network of size {3}: {Netw.is_sorting(Net,3)}")

Net = Netw.empty_network()

print(f"")
print(f"Second case where the network is empty")
print(f"Max: 0")

print(f"The network contains: {Netw.to_string(Net)}")
print(f"")

print(f"Is the network able to sort a network of size {0}: {Netw.is_sorting(Net,0)}")

print(f"")
print(f"Third case where the network max_channel is not equal to size-1")

Net = Netw.empty_network()

Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(0,2)
Com_3 = Comp.make_comparator(1,3)

Netw.append(Com_1,Net)
Netw.append(Com_2,Net)
Netw.append(Com_3,Net)


print(f"Max: {Netw.max_channel(Net)}")

print(f"The network contains: {Netw.to_string(Net)}")
print(f"")

print(f"Is the network able to sort a network of size {4}: {Netw.is_sorting(Net,5)}")

print(f"")
print(f"Fourth case where the network is missing one singular comparator")

Net = Netw.empty_network()

Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)

Netw.append(Com_1,Net)
Netw.append(Com_2,Net)

print(f"Max: {Netw.max_channel(Net)}")

print(f"The network contains: {Netw.to_string(Net)}")
print(f"")

print(f"Is the network able to sort a network of size {3}: {Netw.is_sorting(Net,3)}")

print(f"")
print(f"------- test 10 end -------")
print(f"")

print(f"")
print(f"------- test 11 start -------")
print(f"")

print(f"Testing to_program()")
print(f"")

Net = Netw.empty_network()
v = [9,5,8,23]
len_v = len(v)
for i in range(len_v - 1):
    for j in range(len_v - 1):
        Com = Comp.make_comparator(j, j+1)
        Netw.append(Com, Net)
outputs = Netw.to_program(Net, "v", "aux")
print(outputs)

empty_string = ""

for x in range(len(outputs)):
    empty_string += outputs[x]

print(f"list before: {v}")
aux:int
exec(empty_string)
print(f"list after: {v}")

print(f"")
print(f"------- test 11 end -------")

