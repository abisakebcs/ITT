import itertools
data = ['a','b']
cycler = itertools.cycle(data)
result = list(itertools.islice(cycler, 6))
print("Cycles of given data [a, b]:",result)
