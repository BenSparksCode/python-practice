# Sets: unordered, mutable, no duplicates
se = {1,2,2,3,4}
se2 = set("Hello") #or takes an iterable like a list

# Frozen Set: immutable version of a set
froze = frozenset(se)

odds = {1,3,5}
evens = {2,4,6}
primes = {2,3,5}
sub = {2,3}


# Union - adds without duplication
u = odds.union(evens)
print(u)

# Intersection - only common elements between sets
i = odds.intersection(primes)
print(i)

# Difference - items in 1st set, but not in 2nd set
d = odds.difference(primes)
print(d)

# Symmetric difference - all elements unique to only 1 of the 2 sets
s = evens.symmetric_difference(primes)
print(s)

# Subsets and Supersets - checks if set is subset or superset of another set
print(sub.issubset(primes))
print(primes.issuperset(sub))
