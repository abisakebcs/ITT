String = input("Enter the Paragraph:")
Length = len(String)
Words = String.split()
counts = dict()
for word in Words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
rep_count = dict()
for key,value in counts.items():
  if(value > 1):
      print("The word","'",key,"'","repeated",value,"times") 
print("Length of the Paragraph:",Length)
Longest_word = max(Words,key = len)
print("The Word with highest length:",Longest_word)
   
