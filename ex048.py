#use remainder to determine the chinese zodiac
year = int(input('What year is it? '))
if year % 12 == 8:  #if the year 
    print('Dragon')
elif year % 12 == 9:
    print('Snake')
elif year % 12 == 10:
    print('Horse')
elif year % 12 == 11:
    print('Sheep')
elif year % 12 == 12:
    print('Monkey')
elif year % 12 == 13:
    print('Rooster')
elif year % 12 == 14:
    print('Dog')
elif year % 12 == 15:
    print('Pig')
elif year % 12 == 16:
    print('Rat')
elif year % 12 == 17:
    print('Ox')
elif year % 12 == 18:
    print('Tiger')
else:
    print('Hare')