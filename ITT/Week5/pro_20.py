from collections import Counter
from datetime import datetime
logins = [
"2026-03-10 10:00",
"2026-03-10 12:00",
"2026-03-11 09:30",
"2026-03-11 11:45",
"2026-03-11 14:00"
]

hours = [datetime.strptime(l,"%Y-%m-%d %H:%M").hour for l in logins]
print("Most Frequent Login Hour:",Counter(hours).most_common(1))
