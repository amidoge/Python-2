from math import tan, pi
length_of_side = int(input('What is the length of the side? '))
number_of_sides = int(input('How many sides are there? '))
area = number_of_sides * (length_of_side ** 2) / (4 * tan(pi / number_of_sides))
print(f'The area of that polygon is {area:.2f} square units.')