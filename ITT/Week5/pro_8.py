from collections import deque
s = "level"
print("String:",s)
dq = deque(s)
pal = True
while len(dq) > 1:
   if dq.popleft() != dq.pop():
      pal = False
      break
   print("Palindrome" if pal else "Not Palindrome")
