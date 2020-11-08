#find out frequency from a note that the user inputs
note = str(input('What note do you want to know the frequency of? '))
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
if note == 'C4':
    print(C4)
elif note == 'D4':
    print(D4)
elif note == 'E4':
    print(E4)
elif note == 'F4':
    print(F4)
elif note == 'G4':
    print(G4)
elif note == 'A4':
    print(A4)
elif note == 'B4':
    print(B4)
else:
    if note[0] == 'C' and int(note[1]) <= 8 and len(note) == 2:
        frequency = C4 / 2 ** (4 - int(note[1]))
        print(f'{frequency:.2f}')
    else:
        print('Sorry, but I cannot find the frequency of this note.')