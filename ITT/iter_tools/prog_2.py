import itertools

data = '123'
perms = list(itertools.permutations(data))
print("Possible Permutations:")
for p in perms:
   print(''.join(p))
