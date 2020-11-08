grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
points = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]

total = 0
groups = 0
while True:
    grade = input("Letter Grade: ")
    if grade == ' ':
        break
    else:
        grade = grade.upper() #making sure it is not in lowercase otherwise we would have to double our list
        try: #going to try to see if we can find the index of the grade in the list, and then put the same index of the point an add it to the total
            ind = grades.index(grade)
            total += points[ind]
            groups += 1
        except:
            pass #no error message

gpa = total / groups
print(f"The GPA of all your grades is {gpa}!")
            
