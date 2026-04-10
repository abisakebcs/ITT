from collections import Counter
s = "aabbccddeeffgg"
print("STRING:",s)
freq = Counter(s)
result = len(set(freq.values())) == 1
print("EQUAL FREQUENCY:",result)
