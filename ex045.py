#determine where a square on the chess board is black or white from the location of the square which is given by the user
position = str(input('What position on the chess board to you want to determnine the color of? '))
evens = ['2', '4', '6', '8']
#evens = '2468'
odds = ['1', '3', '5', '7']
letter_group_one = ['a', 'c', 'e', 'g']
letter_group_two = ['b', 'd', 'f', 'h']
if position[0] in letter_group_one and position[1] in odds or \
    position[0] in letter_group_two and position[1] in evens:
    print(f'The color of the position "{position}" is black.')
elif position[0] in letter_group_one and position[1] in evens or \
    position[0] in letter_group_two and position[1] in odds:
    print(f'The color of the position "{position}" is white.')
else:
    print("Sorry but that isn't an existing position on a chess board.")