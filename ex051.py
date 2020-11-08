grade = input('What grade did you get? ')
grade = grade.upper()
a_plus = 4.0
a = 4.0
a_minus = 3.7
b_plus = 3.3
b = 3.0
b_minus = 2.7
c_plus = 2.3
c = 2.0
c_minus = 1.7
d_plus = 1.3
d = 1.0
f = 0
if grade == 'A+':
    print(a_plus)
elif grade == 'A':
    print(a)
elif grade == 'A-':
    print(a_minus)
elif grade == 'B+':
    print(b_plus)
elif grade == 'B':
    print(b)
elif grade == 'B-':
    print(b_minus)
elif grade == 'C+':
    print(c_plus)
elif grade == 'C':
    print(c)
elif grade == 'C-':
    print(c_minus)
elif grade == 'D+':
    print(d_plus)
elif grade == 'D':
    print(d)
elif grade == 'F':
    print(f)
else:
    print('Sorry, but the grade you put in does not exist.')