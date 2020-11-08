#assessing employees
rating = float(input('What is the employees rating?'))
performance = ''
if rating == 0.0:
    performance = 'Unacceptable'
elif rating == 0.4:
    performance = 'Acceptable'
elif rating >= 0.6:
    performance = 'Meritorious'
else:
    print('Sorry, but the rating you put does not exist in this program.')
employee_raise = 2400 * rating
print(f'''
Employee Performance and Raise:
=====================================
Employees Rating: {rating},
Employees Performance: {performance},
Employees Raise: ${employee_raise:.2f}.''')