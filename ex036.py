#determine whether a letter from the alphabet is a vowel, consonent, or sometimes can be both (y)
letter = str(input('What letter from the alphabet would you like us to identify? '))
letter = letter.lower()
#vowels = ['a', 'e', 'i', 'o', 'u']
vowels = 'aeiou'
if letter in vowels:
    print(f'The letter {letter} is a vowel!')
elif letter == 'y':
    print(f'The letter {letter} can sometimes be used as a vowel, and sometimes is used as a consonent!')
else:
    print(f'The letter {letter} is a consonent!')