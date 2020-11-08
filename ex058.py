#date entered from user. Write down the day after that
date = input('What is the date? (y-m-d)')

year = str(date[0:4])
month = str(date[5:7])
day = str(date[8:10])

thirty_one_days = [1, 3, 5, 7, 8, 10]
thirty_or_less_days = [4, 6, 9, 11]

if int(year) % 4 == 0 and int(month) == 2 and int(day) == 28: #if it is a leap year and it is feb 28
    day = '29'

elif int(month) in thirty_or_less_days and int(day) == 30: #if a 30 day month is on it's last day
    month = '0' + str(int(month) + 1)
    day = '01'

elif int(month) == 2 and int(day) == 28: #checking if it is febuary 28 (no leap year)
    month = '03'
    day = '01'

elif int(month) in thirty_one_days and int(day) == 31: #checking if 31 day month and it's on it's last day
    month = '0' + str(int(month) + 1)
    day = '01'

elif int(month) == 12 and int(day) == 31: #checking if it is december 31 so it changes the year month and day
    year = str(int(year) + 1)
    month = '01'
    day = '01'

elif int(year) % 4 == 0 and int(month) == 2:
    day = str(int(day) + 1) 

elif len(int(month)) == 2:
    month = str(int(month))

print(f'{year}-{month}-{day}') #printing the outcome