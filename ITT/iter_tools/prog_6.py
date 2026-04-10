import itertools
data = [5, 10, 15]
cyclee = itertools.cycle(data)
print("Cycles of given data [5, 10, 15] upto the given range:")
for _ in range(9):
   print(next(cyclee))
