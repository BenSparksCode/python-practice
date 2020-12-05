# itertools: product, permutations, combinations, accumulate, groupby, infinite

from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
from itertools import groupby
# from itertools import

# product: creates list of tuples forming combos of elements from lists - useful for matrices
a = [2,3,4]
b = [5,6,7]
prod = product(a, b)
print(list(prod))

# permutations: creates list of tuples containing all permutation of elements in a list - include repetitions
perm = permutations(a)
print(list(perm))
perm = permutations(a, 2) #only length 2 perms
print(list(perm))

# combinations: 
comb = combinations(a, 2) #length arg is mandatory for combinations - no repetition
print(list(comb))

# accumulate: 