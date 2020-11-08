error = False
x = int(input("Number: "))
guess = x / 2
while abs((guess * guess) - x) > 10 ** -12: 
    guess = (guess + x / guess) / 2 #average of the numbers is updated to the guess value
    #warning method
    if guess ** 2 != x:
        error = True
        print(f"{x} is not a square number!")
        break
if error == False:
    print(guess)

'''
x was considered "good enough" when the abs val
of the difference of guess * guess and x was less
than or equal to 10 ** -12. 
'''
