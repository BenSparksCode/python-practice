# Lambda: for creating single-use functions, or functions passed to Higher order functions

# multiply
mult = lambda x,y: x*y

print(mult(3,4))

# sorting

li = [(1,2), (3,-15), (2, 100)]
li_sort = sorted(li, key=lambda x: x[1]) #use lambda to sort by y index instead of x

print(li)
print(li_sort)

# mapping

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))