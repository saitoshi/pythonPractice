'''
@name is_leap_year
@desc A function that determines whether "year" is a leap year 
@input year - int of the year 
@return 
'''
def is_leap_year(year):
    leapYear = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leapYear = True
    return leapYear

isBoolean = is_leap_year(2024)
print(isBoolean)