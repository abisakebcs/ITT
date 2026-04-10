from datetime import datetime
d = datetime.strptime("2026-03-10","%Y-%m-%d")
month = d.month - 1 or 12
year = d.year if d.month != 1 else d.year - 1
prev = d.replace(year=year, month=month)
print("Previous Month Date:",prev.strftime("%Y-%m-%d"))
