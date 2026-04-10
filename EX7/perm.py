
from itertools import permutations

s = '123'
p = list(permutations(s))
print()
for x in p:
    print(''.join(x))
print()
