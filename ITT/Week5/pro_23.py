from datetime import datetime
dates = ["2026-03-10","2024-01-01","2025-05-20"]
oldest = min(datetime.strptime(d,"%Y-%m-%d") for d in dates)
print("Oldest Date:",oldest.strftime("%Y-%m-%d"))
