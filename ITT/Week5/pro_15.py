from datetime import datetime, timedelta
today = datetime.today()
print("Next Five Days")
for i in range(1,6):
   print((today + timedelta(days=i)).strftime("%Y-%m-%d"))
