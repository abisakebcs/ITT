String = input("Enter the Paragraph:")
Length = len(String)
Words = String.split()
counts = dict()
for word in Words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print("=====Repeated Words=====")
rep_count = dict()
for key,value in counts.items():
  if(value > 1):
     print("'",key,"'",":",value)
print("====Length of the Paragraph====")
print("Length of the Paragraph:",Length)
print("====Longest Word====")
Longest_word = max(Words,key = len)
print("The Word with highest length:",Longest_word)
print("====Reversed Longest Word====")
Rev_Longest_word ="".join(reversed(Longest_word))
print("The Reversed Word:",Rev_Longest_word)
