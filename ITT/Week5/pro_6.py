from collections import OrderedDict
s = "swiss"
print("STRING:",s)
freq = OrderedDict()
for ch in s:
   freq[ch] = freq.get(ch,0) + 1
for k,v in freq.items():
   if v == 1:
      print("FIRST NON-REPEATING CHAR:",k)
      break
