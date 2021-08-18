from datetime import date                       # importing the date and time library


def ageCalculator(years, months, days):         # creating a function for age calculation
    age_day = 0                                 # initiating calculated age to 0
    age_months = 0
    age_year = 0

    today_day = int(today.strftime("%d"))       # assigning  current date to individual variable for calculation
    today_month = int(today.strftime("%m"))
    today_year = int(today.strftime("%y"))

    if today_day < day:                         # calculation for no of days
        today_day += 31
        age_day = today_day - days
    else:
        age_day = today_day - days

    if today_month < months:                    # calculation for no of months
        today_month += 12
        age_months = today_month - months
    else:
        age_months = today_month - months

    age_year = today_year - years               # no if years

    print(f"your age of today is :{today_year}-{today_month}-{today_day}")


today = date.today()                                                    # today's date
print("today's date is:", today)
birthDate = input('Enter your birth date in YYYY-MM-DD format:')        # taking input of date from user
year, month, day = map(int, birthDate.split('-'))
if month > 12 or day > 31 or year < int(today.strftime("%y")):          # invalid date checking
    print('invalid date')
    exit()
print("your date of birth is:", birthDate)
ageCalculator(year, month, day)                                         # calling function
