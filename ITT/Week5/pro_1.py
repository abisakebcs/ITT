from collections import Counter
nums = [5,3,5,2,3,1,4,1,2]
print("ARRAY:",nums)
count = Counter(nums)
unique = [num for num in nums if count[num] == 1]
print("UNIQUE ELEMENT:",unique)
