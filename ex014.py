FORMULA = 2.54
feet = input('How much feet tall are you (no inches)')
inches = input('Now tell me how many inches plus your feet are you?')
feet = int(feet)
inches = int(inches)
feet_in_inches = feet * 12
total_inches = feet_in_inches + inches
centimeters = total_inches * FORMULA
print(centimeters)
print(f'{feet} feet and {inches} inches in centimeters is {centimeters:.2f} centimeters!')