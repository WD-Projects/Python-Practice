from datetime import datetime, date, time, timedelta
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.date())
print(datetime.now().time())
print(now.strftime("%B %d, %Y"))

ekhon = date.today()
print(ekhon)

ekhon = date(year = 1999, month = 4, day = 12)
print(ekhon)
print(ekhon.year)

#"timedelta" is basically a difference between present time and future time
ekhon = datetime.now()
print(ekhon + timedelta(days = 5, minutes = 5))