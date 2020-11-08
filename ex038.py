#display days from a month that the user inputs
month = str(input('What month of the year do you want to use?'))
month = month.lower() #this is to make sure that capitals are irrelevant
if month == 'february':
    print('28 or 29 days.')
elif month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
    print('31 days')
else:
    print('30 days')