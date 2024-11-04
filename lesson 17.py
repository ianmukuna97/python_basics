#dates
from datetime import date, timedelta

today = date.today()
print(today)

formatted_date = today.strftime("%Y") # 19-01-2024
print(formatted_date)

after_forty_days = today + timedelta(days=40) # Ctl + Click
print(after_forty_days)


