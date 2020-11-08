from random import randint #going to use 1 and 2 to represent heads or tails
#for one round of coin flip
#variables:
flip_count = 0
total_flips = 0
consecutive_count = 0 #this is zero because we don't even have a flip yet.


for i in range(10): #doing this 10 times
    #in the beginning of the line, we should have some sort of number to compare to the first toss in the line, so that way it would count as the first consecutive number
    h_or_t = randint(1, 2) #heads is 1 tails is 2 
    last_num = h_or_t
    consecutive_count = 1 #because this is the first number in the consecutive series
    #need to print it out:
    if h_or_t == 1:
            print('H', end=' ')
    if h_or_t == 2:
            print("T", end=' ')
    #ONE LINE LOOP UNTIL THERE ARE 3 CONSECUTIVE NUMBERS:
    while consecutive_count != 3: 
        h_or_t = randint(1, 2) #heads is 1 tails is 2
        #COMPARISON
        if h_or_t == last_num:
            consecutive_count += 1
            last_num = h_or_t #setting last_num to the new heads or tails
        else:
            #set it back to one because it is going to be the first consecutive number in the series
            consecutive_count = 1 #because it is going to be the first in the series of consecutive numbers, we set it to one
            last_num = h_or_t #going to set this also to compare
        #PRINTING
        if h_or_t == 1:
            print('H', end=' ')
        if h_or_t == 2:
            print("T", end=' ')
        flip_count += 1 #counting the flips
    #printing the number of flips
    print(f"({flip_count} Flips)")
    total_flips += flip_count #this is for the average in the end. I am going to add them all up, and then divide it by 10 (since there are 10 groups.)
    #also setting flip_counts to zero so that we can count the number of flips per line
    flip_count = 0
#printing the average
print(f'On average, {total_flips / 10} flips were needed.')