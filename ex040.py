#classify a triangle based on the length of each side that the user inputs
side1 = int(input('What is the length of the first side?'))
side2 = int(input('What is the length of the second side?'))
side3 = int(input('What is the length of the third side?'))

if side1 == side2 and side1 == side3:
    print('All the sides are the same length. So it is a equivalent triangle.')
elif side1 != side2 and side2 != side3 and side1 != side3:
    print('All the sides have different length. So it is a scalene triangle.')
else:
    print('Two of the sides have the same length and the other one does not. So it is an is an isosceles triangle.')
