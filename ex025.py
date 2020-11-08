MINUTE = 60
HOUR = 3600
DAY = 86400
SECONDS = 1
seconds = int(input('How many seconds do you want us to calculate? '))

day_amount = seconds // DAY
extra_seconds = seconds % DAY

hour_amount = extra_seconds // HOUR
extra_seconds = extra_seconds % HOUR

minute_amount = extra_seconds // MINUTE
extra_seconds = extra_seconds % MINUTE

second_amount = extra_seconds // SECONDS


print(f'{day_amount:02d}:{hour_amount:02d}:{minute_amount:02d}:{second_amount:02d}') #the :02d will give us 2 spaces with a 0 on the top