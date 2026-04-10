from collections import defaultdict
words = ["python","java","go","c","ruby","php"]
print("PROG_LANG_ARRAY:",words)
group = defaultdict(list)
for w in words:
   group[len(w)].append(w)
for k,v in sorted(group.items()):
   print(k,"→",v)
