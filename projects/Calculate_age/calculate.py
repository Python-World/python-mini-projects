import datetime
from datetime import date 

# returns age
def calculate_age(born): 
	today = date.today() 
	try: 
		birthday = born.replace(year = today.year) 

	# raised when birth date is February 29 and the current year is not a leap year 
	except ValueError: 
		birthday = born.replace(year = today.year, month = born.month + 1, day = 1) 

	if birthday > today: 
		return today.year - born.year - 1
	else: 
		return today.year - born.year

name = input("input your name: ")
#enter in format YYYY-MM-DD
#example 1997-02-03
dob = input("input your date of birth: ")
y = int(dob[:4])
m = int(dob[5:7])
d = int(dob[8:])
res = calculate_age(date(y,m,d))
mon = res*12+(12-m)
birth_date = datetime.date(y,m,d)
today_date = date.today()
day = (today_date-birth_date).days
hrs = day*24
min = hrs*60
print("%s's age is %d years or " % (name, res), end="")
print("%d months or %d days or " % (mon,day), end ="")
print("%d hours or %d minutes" % (hrs,min))

