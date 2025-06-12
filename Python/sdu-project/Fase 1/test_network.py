from network import *
import comparator_rev_5 as Comp
import network_rev_4 as Comp1
import random
print(f"------- test 1 start -------")
Net_1 = empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)
Com_3 = Comp.make_comparator(0,2)
append(Com_1,Net_1)
append(Com_2,Net_1)
append(Com_3,Net_1)

v=[1,2,0,4]
print(f"List listi contains before: {v}\n")
print(f"List listi contains after: {apply(Net_1,v)}")
print(f"------- test 1 end -------")
print(" ")
print(f"------- test 2 start -------")
Net_2 = empty_network()
u=[10,9,8,7,6,5,4,3,2,1,0]
lengd=len(u)
for i in range(lengd-1):
    for j in range(lengd-1):
        Com_4 = Comp.make_comparator(j,j+1)
        append(Com_4,Net_2)

#append(Comp.make_comparator(lengd,lengd-1),Net_2)
print(f"List listi contains before: {u}\n")
print(f"List listi contains after: {apply(Net_2,u)}")
print(f"------- test 2 end -------")
print(" ")




print(f"------- test 3 start -------")
Net_2 = empty_network()
u=[]
for i in range(50):
    u.append(random.randint(0,100))
lengd=len(u)
for i in range(lengd-1):
    for j in range(lengd-1):
        Com_4 = Comp.make_comparator(j,j+1)
        append(Com_4,Net_2)
print(Net_2)
print(f"List listi contains before: {u}\n")
print(f"List listi contains after: {apply(Net_2,u)}")
print(f"------- test 3 end -------")



print(f"------- test 4 start -------")
print(f"This is the network and list from the first project introduction")
print(" ")
Net_4 = empty_network()
Com_10 = Comp.make_comparator(0,1)
Com_20 = Comp.make_comparator(2,3)
Com_30 = Comp.make_comparator(0,2)
Com_40 = Comp.make_comparator(1,3)
Com_50 = Comp.make_comparator(3,4)
Com_60 = Comp.make_comparator(1,2)
Com_70 = Comp.make_comparator(1,3)
Com_80 = Comp.make_comparator(2,3)
Com_90 = Comp.make_comparator(0,1)

append(Com_10,Net_4)
append(Com_20,Net_4)
append(Com_30,Net_4)
append(Com_40,Net_4)
append(Com_50,Net_4)
append(Com_60,Net_4)
append(Com_70,Net_4)
append(Com_80,Net_4)
append(Com_90,Net_4)

t=[9,2,7,4,1]
print(f"List listi contains before: {t}\n")
print(f"List listi contains after: {apply(Net_4,t)}")
print(f"------- test 4 end -------")
print(" ")
print(f"------- test 5 start -------")
print(f" To_program() test")
print(" ")
print(Comp1.to_program(Net_4,"var","aux"))

print(f"------- test 5 end -------")
print("")
print(f"------- test 6 start -------")
print(f" To_program() test")
print(" ")
out_put=Comp.to_program(Com_90,"var","aux")
n_string=""
for i in range(len(out_put)):
    n_string+=out_put[i] + "\n"
var=[9,5,8,23,7,9,4]
print("var before:  ",var)
aux:int
c=Comp.make_comparator(0,1)
exec(n_string)
print("var after:   ",var)
print(f"------- test 6 end -------")
print(" ")


print(f"------- test 7 start -------")
print(f" To_program() in network.py test")
print(" ")
Net_99 = empty_network()
tp_list=[9,5,8,23,7,9,4]
lengd=len(tp_list)
for i in range(lengd-1):
    for j in range(lengd-1):
        Com_4 = Comp.make_comparator(j,j+1)
        append(Com_4,Net_99)
out_puts=Comp1.to_program(Net_99,"tp_list","auxi")
print(out_puts)
ne_string=""
for x in range(len(out_puts)):
    ne_string+=out_puts[x]
print("tp_list before:  ",tp_list)
auxi:int
exec(ne_string)
print("tp_list after:   ",tp_list)
print(f"------- test 7 end -------")