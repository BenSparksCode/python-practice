# Tuple: ordered, immutable, allows duplicate elements
import sys, timeit

tup = (1,2,3,4,5)
li = [1,2,3,4,5]

# splitting tuple out into first and last elements, and list for in-between items
i1, *i2, i3 = tup

print(i1, i2, i3)

# List vs Tuple - Memory Efficiency -> Tuples more memory efficient
print(sys.getsizeof(tup), "bytes")
print(sys.getsizeof(li), "bytes")

# List vs Tuple - Time Efficiency -> Tuples more time efficient
print(timeit.timeit(stmt="(0,1,2,3,4)", number=100000))
print(timeit.timeit(stmt="[0,1,2,3,4]", number=100000))
