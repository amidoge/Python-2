magnitude = float(input('What is the magnitude?'))
descriptor = ''
if magnitude < 2.0:
    descriptor = 'Micro'
elif magnitude == 2.0 or magnitude < 3.0:
    descriptor = 'Very Minor'
elif magnitude == 3.0 or magnitude < 4.0:
    descriptor = 'Minor'
elif magnitude == 4.0 or magnitude < 5.0:
    descriptor = 'Light'
elif magnitude == 5.0 or magnitude < 6.0:
    descriptor = 'Moderate'
elif magnitude == 6.0 or magnitude < 7.0:
    descriptor = 'Strong'
elif magnitude == 7.0 or magnitude < 8.0:
    descriptor = 'Major'
elif magnitude == 8.0 or magnitude < 10.0:
    descriptor = 'Great'
elif magnitude > 10.0:
    descriptor = 'Meteoric'
else:
    print('There is an error with your input. Please try again.')

print(f'The magnitude {magnitude} is {descriptor}.')