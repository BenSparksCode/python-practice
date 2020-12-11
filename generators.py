# Generators: custom iterables that create new objects when required, memory efficient

import sys

def my_gen():
    yield 1
    yield 5
    yield 3

def countdown(n):
    print("Starting")
    while n > 0:
        yield n
        n -= 1

g = my_gen()

for i in g:
    print(i)

g = my_gen()
print(next(g))

# iterable functions work
cd = countdown(5)
print(next(cd))

# array method
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num +=1
    return nums

def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

# When needing to run operation on a predictable list - generators more memory efficient

print(sys.getsizeof(firstn(10000))) # 43808 bytes
print(sys.getsizeof(firstn_gen(10000))) # 56 bytes

# Fibonacci implemented as generator
def fib_gen(lim):
    a, b = 0, 1
    while a < lim:
        yield a
        a,b = b, a+b

f = fib_gen(50)

for i in f:
    print(i)

# generators built similar to list comprehension
odd_gen = (i for i in range(100) if i%2==1)

for i in odd_gen:
    print(i)