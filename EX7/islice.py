from itertools import cycle, islice

l= ['a', 'b']
c= cycle(l)
r= list(islice(c, 6))
print()
print(r)
print()
