from datetime import datetime
d = datetime.strptime("2026-03-14","%Y-%m-%d")
print(d)
if d.weekday() >= 5:
   print("Weekend")
else:
   print("Weekday")
