#write a program which tells you the Holiday based on the date which is entered from the user
month = str(input('What is the month for the national holiday? '))
day = int(input('What day in the month? '))
month = month.lower()
new_years_day = ['january', 1]
canada_day = ['july', 1]
christmas = ['december', 25]
if month in new_years_day and day in new_years_day:
    print('New Years Day!')
elif month in canada_day and day in canada_day:
    print('Canada Day!')
elif month in christmas and day in christmas:
    print('Christmas!')
else:
    print('There is no national holiday in Canada in the date given.')
