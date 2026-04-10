from itertools import count

c = count(10)
r = [next(c) for _ in range(5)]
print()
print(r)
print()
