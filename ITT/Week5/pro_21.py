from collections import Counter
from datetime import datetime
events = [
"2025-01-10",
"2025-01-20",
"2025-02-05",
"2025-02-15","2025-03-01"
]
months = [datetime.strptime(e,"%Y-%m-%d").strftime("%B") for e in events]
print("Monthly Event Counter:",Counter(months))
