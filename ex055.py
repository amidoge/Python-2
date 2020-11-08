#frequency to name
frequency = float(input('What is the frequency?'))
if frequency < 3 * 10 ** 9:
    print('Radio Waves')
elif frequency < 3 * 10 ** 12:
    print('Microwaves')
elif frequency < 4.3 * 10 ** 14:
    print('Infrared Light')
elif frequency < 7.5 * 10 ** 14:
    print('Visible light')
elif frequency < 3 * 10 ** 17:
    print('Ultra Violet Light')
elif frequency < 3 * 10 ** 19:
    print('X-Rays')
elif frequency >= 3 * 10 ** 19:
    print('Gamma Rays')
else:
    print('Sorry, there is an errror with your input.')