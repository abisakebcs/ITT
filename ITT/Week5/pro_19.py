from collections import Counter
from datetime import datetime
logins = [
"2026-03-10 10:00",
"2026-03-10 12:00",
"2026-03-11 09:30",
"2026-03-11 11:45",
"2026-03-11 14:00"
]
dates = [datetime.strptime(l,"%Y-%m-%d %H:%M").date() for l in logins]
print("Daily Login Counter:",Counter(dates))
