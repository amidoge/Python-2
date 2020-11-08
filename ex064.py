total = 0
while True:
    price = input("What is the price? (leave blank to stop)")
    if price == ' ':
        break
    else:
        total += int(price)
if total == 0:
    print("Please enter a price before you choose to stop.")
else:
    total = str(total)#making it to string so that I can access the last digit
    total_numbers = [] #making list to put the each digit of total into different indexes
    for i in range(len(total)): #for loop for putting total digits into different indexes in the list
        total_numbers.append(total[i])
        #CONDITIONALS FOR ROUNDING
    if int(total[-1]) < 3 or int(total[-1]) >= 8: 
        total_numbers[-1] = '0'
    elif int(total[-1]) >= 3 or int(total[-1]) <= 7:
        total_numbers[-1] = '5'
        #PRINTING NEW ROUNDED TOTAL
    rounded_total = ''
    for i in range(len(total)):
        rounded_total = rounded_total + str(total_numbers[i]) #ADDING THE DIGITS OF TOTAL AND THE ROUNDED NUMBER TO A NEW VARIABLE
    total = float(total) #CHANGING TOTAL TO FLOAT SO I CAN GET THE .00 PART
    rounded_total = float(rounded_total) #DOING THE SAME THING AS BEFORE
    print(f"${total:.2f}") #PRINTING THE VALUES
    print(f"${rounded_total:.2f}")