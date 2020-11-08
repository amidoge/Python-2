from random import randint
random_int = randint(1, 100) #need to get a number to store to maximum_int, so that we can compare it with the next 99 numbers
maximum_int = random_int
print(maximum_int) #must also print the maximum integer first otherwise I will only have 99 numbers and not 100
update_count = 0
for i in range(99): #99 because we already did a random_int once before for comparison to the others.
    random_int = randint(1, 100)
    if random_int > maximum_int:
        update_count += 1 #we want to count how many times the maximum_number updated, to show the user how many times it did, whenm every number was being generated.
        maximum_int = random_int
        print(f"{maximum_int} <== Update") #need to include the Update to show that the maximum number has changed
    else:
        print(random_int) #otherwise. I don't print the maximum integer (new) but print the random_int generated

#after the loop, I should have the maximum int ever generated on that list stored on maximum_int variable
#I should also have the count of the number of times it updated stored in update_count variable
print(f"The maximum value found was {maximum_int}")
print(f"The maximum value was updated {update_count} times")