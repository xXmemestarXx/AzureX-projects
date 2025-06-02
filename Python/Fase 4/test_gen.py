import filter_new as Filt
import comparator2 as Comp
import generate2 as Gene

n = 3
filt_test = Filt.make_empty_filter(n)
w = [filt_test]
filt_test2 = Gene.extend(w, n)
print(filt_test)
print(filt_test2)

