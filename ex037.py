# determine a shape from 1 to 10 from the number of sides
sides = int(input('How many sides does your shape have? '))
if sides == 3:
    print('The shape is a triangle.')
elif sides == 4:
    print('The shape is a square.')
elif sides == 5:
    print('The shape is a pentagon')
elif sides == 6:
    print('The shape is a hexagon.')
elif sides == 7:
    print('The shape is a heptagon.')
elif sides == 8:
    print('The shape is a octogon.')
elif sides == 9:
    print('The shape is a nonagon.')
elif sides == 10:
    print('The shape is a decagon.')
else:
    print('Sorry, but you can only put in 3 to 10 sides.')