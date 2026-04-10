from collections import Counter
dates = ["2026-03-10","2026-03-10","2026-03-11"]
dup = [d for d,c in Counter(dates).items() if c > 1]
print("Duplicate Dates:",dup)
