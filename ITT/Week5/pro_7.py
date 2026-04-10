from collections import deque
nums = [1,2,3,4,5,6]
window = 3
dq = deque()
sum_window = 0
for i in range(len(nums)):
   dq.append(nums[i])
   sum_window += nums[i]
   if len(dq) == window:
      print("SLIDING WINDOW SUM:",sum_window)
      sum_window -= dq.popleft()
