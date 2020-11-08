YARDS = 0.33333333
MILES = 0.00018939
INCHES = 12
feet = input('How much feet do you want us to calculate in yards, miles, and inches? ')
feet = float(feet)
inches = feet * INCHES
miles = feet * MILES
yards = feet * YARDS
print('\nCalculating Measurements...\n')
print(f'It would take {inches} inches to equal {feet} feet.') 
print(f'It would take {yards} yards to equal {feet} feet.') 
print(f'It would take {miles} miles to equal {feet} feet.') 