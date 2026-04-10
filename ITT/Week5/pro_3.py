from collections import Counter
list1 = [1,2,3,4,5]
list2 = [1,2,2,3,4,4,5]
print("LIST 1:",list1)
print("LIST 2:",list2)
c1 = Counter(list1)
c2 = Counter(list2)
extra = c2 - c1
print("EXTRA ELEMENTS:",list(extra.elements()))
