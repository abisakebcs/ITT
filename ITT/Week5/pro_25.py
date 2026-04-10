from datetime import datetime, timedelta
activities = {
"A":"2026-03-25 10:00",
"B":"2026-03-26 08:00",
"C":"2026-03-24 09:00"
}
now = datetime.strptime("2026-03-26 12:00","%Y-%m-%d %H:%M")
recent = []
for user,time in activities.items():
   t = datetime.strptime(time,"%Y-%m-%d %H:%M")
   if now - t <= timedelta(days=1):
      recent.append(user)
print("Recent Activity:",recent)
