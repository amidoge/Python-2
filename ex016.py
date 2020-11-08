from math import pi
radius = input('What is the radius you want us to use? ')
radius = float(radius)
area = pi * (radius ** 2)
volume = (4 / 3) * pi * (radius ** 3)
print(f'\nThe area of a circle using the radius is {area:.2f} square units, and the volume of a sphere using the radius would be {volume:.2f} cubic units\n')