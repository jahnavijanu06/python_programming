def is_leap_year(year):
    if(year%4 == 0):
       return True
    else:
        return False


year =int(input("enter a year: "))
if is_leap_year(year):
    print("{a} is a leap year. ".format(a=year))
else:
    print("{a} is not a leap year.".format(a=year))
