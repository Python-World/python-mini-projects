year = int(input("Enter a year:- "))   # Here, you take the input from the user

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):   
    """
    if a year is a multiple of four and a multiple of 100 i.e. if it is a multiple of 400 it is not a leap year
    """
    print("{0} is a leap year!!".format(year))
    """
    printing the output
    """
else:
    print("{0} is not a leap year!!".format(year))
