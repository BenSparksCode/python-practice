# itertools: product, permutations, combinations, accumulate, groupby, infinite

from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
import operator #for changing accumulate operation
from itertools import groupby

# product: creates list of tuples forming combos of elements from lists - useful for matrices
a = [2,3,4,3]
b = [5,6,7]
prod = product(a, b)
print(list(prod))

# permutations: creates list of tuples containing all permutation of elements in a list - include repetitions
perm = permutations(a)
print(list(perm))
perm = permutations(a, 2) #only length 2 perms
print(list(perm))

# combinations: creates list of tuples of all cominations - length needed
comb = combinations(a, 2) #length arg is mandatory for combinations - no repetition
print(list(comb))

# accumulate: creates list where items are sum of prev items - cumulative data
acc = accumulate(a)
print(list(acc))
acc = accumulate(a, func=operator.mul) # sets operation to multiply, not adding
print(list(acc))
acc = accumulate(a, func=max) # sets operation to finding max in list so far
print(list(acc))

# groupby: groups list items into separate lists based on a decision function
a = [1,2,3,4]

group_obj = groupby(a, key=lambda x: x<3)

for key, val in group_obj:
    print(key, list(val))
