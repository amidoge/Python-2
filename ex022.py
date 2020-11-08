#finding the area of the triangle again
#this time we are going to find the area from finding out each side of the triangle
from math import sqrt
s1 = float(input('What is the length of the first side? '))
s2 = float(input('What is the length of the second side? '))
s3 = float(input('What is the length of the third side? '))
s = (s1 + s2 + s3)/2
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))
print(f'{area:.2f}')