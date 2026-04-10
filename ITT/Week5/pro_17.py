from datetime import date, timedelta
start = date(2025,1,1)
end = date(2025,1,31)
count = 0
while start <= end:
   if start.weekday() == 6:
      count += 1
   start += timedelta(days=1)
print("Sundays Count:",count)
