#same thing as exercise 46 except you determine the zodiac sign
month = str(input('What month were you born? '))
month = month.lower()
day = int(input('What day were you born? '))

if month == 'december' and day >= 22 or month == 'january' and day <= 19:
    print('Your astrological sign is Capricorn!')
elif month == 'january' and day >= 20 or month == 'febuary' and day <= 18:
    print('Your astrological sign is Aquarius!')
elif month == 'febuary' and day >= 19 or month == 'march' and day <= 20:
    print('Your astrological sign is Pisces!')
elif month == 'march' and day >= 20 or month == 'april' and day <= 19:
    print('Your astrological sign is Aries!')
elif month == 'april' and day >= 20 or month == 'may' and day <= 20:
    print('Your astrological sign is Taurus!') 
elif month == 'may' and day >= 21 or month == 'june' and day <= 20:
    print('Your astrological sign is Gemini!')
elif month == 'june' and day >= 21 or month == 'july' and day <= 22:
    print('Your astrological sign is Cancer!')
elif month == 'july' and day >= 23 or month == 'august' and day <= 22:
    print('Your astrological sign is Leo!')
elif month == 'august' and day >= 23 or month == 'september' and day <= 22:
    print('Your astrological sign is Virgo!')
elif month == 'september' and day >= 23 or month == 'october' and day <= 22:
    print('Your astrological sign is Libra!')
elif month == 'october' and day >= 23 or month == 'november' and day <= 21:
    print('Your astrological sign is Scorpio!')
elif month == 'november' and day >= 22 or month == 'december' and day <= 21:
    print('Your astrological sign is Sagittarius!')