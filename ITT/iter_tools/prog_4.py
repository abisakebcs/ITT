import itertools
counter = itertools.count(start=10)
five = [next(counter) for _ in range(5)]

print("Count of Numbers from start to given range:",five)
