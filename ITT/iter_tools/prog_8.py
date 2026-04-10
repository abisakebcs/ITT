from itertools import product
colors = ['red', 'green', 'blue']
combinations = product(colors, repeat=2)
print("All possible product combinations:")
for combo in combinations:
    print(combo)
