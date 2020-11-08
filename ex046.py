#determine the season based on a date
month = str(input('What is the month?'))
day = int(input('What is the day of the month?'))
month = month.lower()

spring = ['march', 'april', 'may']

summer = ['june', 'july', 'august']

fall = ['september', 'october', 'november']

winter = ['december', 'january', 'febuary']

#SPRING
if month in spring or month == 'march' and day >= 20:
    print(f'{month} {day} is in Spring.')
elif month == 'june' and day < 21:
    print(f'{month} {day} is in Spring.')
#SUMMER
elif month in summer or month == 'june' and day >= 21:
    print(f'{month} {day} is in Summer.')
elif month == 'september' and day < 22:
    print(f'{month} {day} is in Summer.')
#FALL
elif month in fall or month == 'september' and day >= 22:
    print(f'{month} {day} is in Fall.')
elif month == 'december' and day < 21:
    print(f'{month} {day} is in Fall.')
#WINTER
elif month in winter or month == 'december' and day >= 21:
    print(f'{month} {day} is in Winter.')
elif month == 'march' and day < 20:
    print(f'{month} {day} is in Winter.')
else:
    print('That date does not exist.')