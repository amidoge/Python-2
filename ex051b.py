grade = input('What grade did you get? ')
grade = grade.upper()
grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
points = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]

try:
    n = grades.index(grade)
    print(points[n])
except ValueError:
    print('Sorry, but the grade does not exist.')