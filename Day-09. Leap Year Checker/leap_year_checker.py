def is_leap_year(y):
    if (y % 400 == 0):
        return f'{y} is leap year.'
    elif(y % 100 == 0):
        return f'{y} is not a leap year'
    elif (y % 4 == 0):
        return f'{y} is a leap year'
    else:
        return f'{y} is not a leap year'

year = int(input('Enter year: '))
print(is_leap_year(year))