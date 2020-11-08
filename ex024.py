#Create a program that reads a duration from the user as a number of days, hours, minutes,and
# seconds. Compute and display the total number of seconds represented by this duration.
MINUTE = 60
HOUR = 3600
DAY = 86400
days = int(input('How many days? '))
hours = int(input('How many hours? '))
minutes = int(input('How many minutes? '))
seconds = int(input('How many seconds? '))
total_seconds = (DAY * days) + (HOUR * hours) + (MINUTE * minutes) + seconds
print(f'The total amount of seconds {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds, is {total_seconds} seconds')
