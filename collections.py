# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# Counter: converts iterable into dictionary of counts of each element
a = "aaabbcccccc"
count = Counter(a)
print(count)
print(count.most_common(1)) # Gets n most common items

# namedtuple: creates a subclass of Tuple with named properties
Point = namedtuple("Point", "x,y")
pt = Point(1,-4)
print(pt)
print(pt.x)

# OrderedDict: Ordered version of dictionary. Normal dictionaries ordered since Python 3.7
# Just using normal dicts for this since 3.7

# defaultdict: creates dictionary with specied type for each element
defd = defaultdict(int)
defd["a"] = 1
defd["b"] = 2
print(defd)

# deque = double-ended queue. Very efficient and useful.
d = deque()
d.append(1) #Add on right
d.append(2)
print(d)
d.appendleft(3) #Add on left
d.appendleft(4)
print(d)
print(d.pop()) #remove from right
print(d.popleft()) #remove from left
print(d)
d.clear() #clear completely
print(d)
d.extend([1,2,3]) #add 1 at a time onto right
d.extendleft([4,5,6]) #add 1 at a time onto left
print(d)
d.rotate(2) #take items from right and add to left
print(d)
d.rotate(-1) #take items from left and add to right
print(d)



