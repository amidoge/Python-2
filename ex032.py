#read 3 different integers and list them from smallest to largest using the min() and max() functions
num_1 = int(input('What is the first integer?'))
num_2 = int(input('What is the second integer?'))
num_3 = int(input('What is the third integer?'))

highest = max(num_1, num_2, num_3)
lowest = min(num_1, num_2, num_3)
middle = num_1 + num_2 + num_3 - lowest - highest

print(f'''
The order from the numbers you gave me from the lowest value to the greatest value is...
{lowest}, {middle}, and {highest}
''')