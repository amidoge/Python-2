import sys

#find out how many dog years your dog is. (first two years are each 10.5 and the rest are +4)
human_years = float(input('How many human years has your dog been alive for? '))

# if invalid input, stop
if human_years <= 0:
    print('We cannot use a number which is smaller or equivalent to zero.')
    # exit program
    sys.exit()

# process as usual
dog_years = 0
if human_years <= 2 and human_years > 0: # 0 <= human_years <= 2
    dog_years += 10.5 * human_years
else:
    dog_years += 21
    human_years -= 2
    dog_years += human_years * 4 
print(f'Your dog is {dog_years} years old!')