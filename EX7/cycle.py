
from itertools import cycle

l= [5, 10, 15]
c= cycle(l)
r= [next(c) for _ in range(9)]
print()
print(r)
print()
