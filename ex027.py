# finding body mass index
height = float(input('What is your height in meters? '))
weight = float(input('What is your weight in kg? '))
BMI = weight / (height * height)
print(f'You have a BMI of {BMI:.2f}')