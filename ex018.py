from math import pi
height = float(input('What is the height of your cylinder? '))
radius = float(input('What is the radius of you cylinder? '))
area_of_base = pi * (radius ** 2)
volume = area_of_base * height
print(f'\nIf the radius = {radius} and the height = {height}, then the volume of your cylinder is {volume:.2f}\n')