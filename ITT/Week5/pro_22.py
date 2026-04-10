from collections import defaultdict
from datetime import datetime
dates = ["2026-03-10","2026-03-11","2026-03-12"]
group = defaultdict(list)
for d in dates:
   day = datetime.strptime(d,"%Y-%m-%d").strftime("%A")
   group[day].append(d)
print("Group Dates by Weekday:",dict(group))
