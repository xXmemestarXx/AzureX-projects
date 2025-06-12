import comparator as Comp
import network as Netw
import filter as Filt
import generate as Gene

print(f"")
print(f"------- test filter.py -------")
print(f"")
print(f"------- test 1 begin -------")
print(f"")
print(f"Testing make_empty_filter()")
print(f"")

filt_test = Filt.make_empty_filter(0)
filt_test2 = Filt.make_empty_filter(2)
print(f"{filt_test} => {filt_test}")
print(f"{filt_test2} => {filt_test2}")

print(f"")
print(f"------- test 1 end -------")
print(f"")

print(f"------- test 2 begin -------")
print(f"")
print(f"Testing net()")
print(f"")

comp_test = Comp.make_comparator(0, 1)
filt_test = Filt.make_empty_filter(0)
filt_test2 = Filt.make_empty_filter(2)
filt_test2 = Filt.add(comp_test, filt_test2)
print(f"{filt_test} => {Filt.net(filt_test)}")
print(f"{filt_test2} => {Filt.net(filt_test2)}")
print(f"")
print(f"------- test 2 end -------")
print(f"")

print(f"------- test 3 begin -------")
print(f"")
print(f"Testing out()")
print(f"")

filt_test = Filt.make_empty_filter(0)
filt_test2 = Filt.make_empty_filter(2)
print(f"{filt_test} => {Filt.out(filt_test)}")
print(f"{filt_test2} => {Filt.out(filt_test2)}")
print(f"")
print(f"------- test 3 end -------")
print(f"")

print(f"------- test 4 begin -------")
print(f"")
print(f"Testing size()")
print(f"")

filt_test = Filt.make_empty_filter(0)
filt_test2 = Filt.make_empty_filter(2)
print(f"{filt_test} => size(filter) => {Filt.size(filt_test)}")
print(f"{filt_test2} => size(filter) => {Filt.size(filt_test2)}")
print(f"")
print(f"------- test 4 end -------")
print(f"")

print(f"------- test 5 begin -------")
print(f"")
print(f"Testing is_redundant()")
print(f"")

filt_test = Filt.make_empty_filter(3)

filt_test2 = Filt.make_empty_filter(3)
filt_test2 = Filt.add(2, filt_test)

# Doing this to minmize length of the statement
print_help = Filt.is_redundant(2, filt_test)
print_help2 = Filt.is_redundant(2, filt_test2)

print(f"{filt_test} => Testing a single comparator => {print_help}")
print(f"{filt_test2} => Testing duplicated comparators => {print_help2}")
print(f"")
print(f"------- test 5 end -------")
print(f"")

print(f"------- test 5 begin -------")
print(f"")
print(f"Testing add()")
print(f"")

filt_test = Filt.make_empty_filter(2)
filt_test2 = Filt.make_empty_filter(2)
filt_test2 = Filt.add(2, filt_test2)

print(f"{filt_test} => add(2, filter) => {filt_test2}")

print(f"------- test 5 end -------")
print(f"")

print(f"------- test 6 begin -------")
print(f"")
print(f"Testing is_sorting()")
print(f"")

filt_test = Filt.make_empty_filter(4)
filt_test = Filt.add(2, filt_test)
filt_test = Filt.add(5, filt_test)
filt_test = Filt.add(8, filt_test)

filt_test2 = Filt.make_empty_filter(3)
filt_test2 = Filt.add(2, filt_test2)
filt_test2 = Filt.add(5, filt_test2)
filt_test2 = Filt.add(8, filt_test2)

print(f"{filt_test} => is_sorting(filter) => {Filt.is_sorting(filt_test)}")
print(f"{filt_test2} => is_sorting(filter) => {Filt.is_sorting(filt_test2)}")

print(f"------- test 6 end -------")
print(f"")

print(f"")
print(f"------- test generate.py -------")
print(f"")
print(f"------- test 1 begin -------")
print(f"")
print(f"Testing extend()")
print(f"")

F1 = Filt.add(2,Filt.make_empty_filter(3))
F2 = Filt.add(5,Filt.make_empty_filter(3))
F3 = Filt.add(8,Filt.make_empty_filter(3))

all_filters = [F1,F2,F3]

for i in range(0,len(all_filters)):
    print(f"Filter {i+1} network:{Filt.net(all_filters[i])} => {Filt.out(all_filters[i])}\n")

new = Gene.extend(all_filters,3)

print("After Extending")

for i in range(0,len(new)):
    print(f"Filter {i+1} network:{Filt.net(new[i])} => {Filt.out(new[i])}\n")

print(f"")
print(f"------- test 1 end -------")
print(f"")
