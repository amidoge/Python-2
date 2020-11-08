#roulette simulator
from random import randint
green = [0, 00]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 ]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35]
number = randint(0, 37) #random number from 0 to 37 (37 represents 00)
color = ''
evenorodd = ''
numtonum = ''
number = 37
if number == 0:
    print('The spin resulted in 0...')
    print('Pay 0')
elif number == 37:
    print('The spin resulted in 00...')
    print('Pay 00')

if number in red:
    color = 'Red'
elif number in black:
    color = 'Black'

if number % 2 == 0:
    evenorodd = 'Even'
elif number % 2 == 1:
    evenorodd = 'Odd'

if number <= 18 and number >= 1:
    numtonum = '1 to 18'
    print(f'''
The spin resulted in {number}...
Pay {number}
Pay {color}
Pay {evenorodd}
Pay {numtonum}
''')
elif number >= 19 and number <= 36:
    numtonum = '19 to 36'
    print(f'''
The spin resulted in {number}...
Pay {number}
Pay {color}
Pay {evenorodd}
Pay {numtonum}
''')