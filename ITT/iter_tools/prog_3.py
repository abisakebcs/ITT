import itertools

data = [1, 2]
combos = list(itertools.combinations_with_replacement(data, 2))
print("Combinations with Replacements:",combos)
