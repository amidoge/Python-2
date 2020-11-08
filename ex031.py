number = str(input('What is the 4 digit number you want us to use? '))
total = 0

for i in range(len(number)):
    total += int(number[i])
    if i == len(number) - 1:
        print(f'{number[i]}={total}')
        break
    print(number[i], end='+')
    
