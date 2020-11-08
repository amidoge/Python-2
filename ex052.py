#grade points to letter grade
grade_point = float(input('What grade point did you get?'))

points = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]
grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']

try:
    x = points.index(grade_point)
    print(grades[x])
except ValueError:
    print('Sorry, but we do not have that grade point in this program')
