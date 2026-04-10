from datetime import datetime
d = datetime.strptime("2026-03-10","%Y-%m-%d")
print("Week Number:",d.strftime("%U"))
