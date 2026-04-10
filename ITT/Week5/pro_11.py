import datetime
year = 2028
print("Year:",year)
is_leap = datetime.date(year,1,1).replace(year=year).year % 4 == 0 and \
(year % 100 != 0 or year % 400 == 0)
print("Leap Year:",is_leap)
