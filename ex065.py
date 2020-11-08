x_coordinates = []
y_coordinates = []
round = 0
while True:
    x = input("Enter the x part of the coordinate (blank to quit): ")
    if x == ' ' and round == 0: #if there is a blank coordinate on the first input then we should give a appropriate error message
        print("Sorry but you cannot enter a blank coordinate on the first input.")
        break
    elif x == ' ' and round != 0: #if it is just blank but not on the first round, then we should leave again, except without an error message
        break
    y = input("Enter the y part of the coordinate: ")
    if x != ' ': #if the x is not empty (must be a number in there) then I want to add it to the list
        x_coordinates.append(int(x))
        y_coordinates.append(int(y))
        round += 1
        

print(x_coordinates)
print(y_coordinates)    
perimeter = 0
for i in x_coordinates:
    distance = (x_coordinates[i + 1] - x_coordinates[i]) ** 2 + (y_coordinates[i + 1] - y_coordinates[i]) ** 2
    perimeter += distance ** 0.5
    print(distance)

print(f'The perimeter of that polygon is {perimeter}') 
    
