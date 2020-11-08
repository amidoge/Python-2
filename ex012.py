from math import *
t1 = float(input('What is your first longitude?'))
t2 = float(input('What is your first latitude?'))
g1 = float(input('What is your second longitude?'))
g2 = float(input('What is your second latitude?'))
# converting the degrees to radians so that it is able to do the formula
radians(t1)
radians(t2)
radians(g1)
radians(g2)
distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) + cos(t2) * cos(g1 - g2))
print(f'The distance from {t1},{g1} to {t2},{g2} is {distance} kilometers!')

