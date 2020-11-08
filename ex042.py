#frequency to note
frequency = float(input('What is the frequency? '))
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
if frequency <= C4 + 1 and frequency >= C4 - 1:
    print('C4')
elif frequency <= D4 + 1 and frequency >= D4 - 1:
    print('D4')
elif frequency <= E4 + 1 and frequency >= E4 - 1:
    print('E4')
elif frequency <= F4 + 1 and frequency >= F4 - 1:
    print('F4')
elif frequency <= G4 + 1 and frequency >= G4 - 1:
    print('G4')
elif frequency <= A4 + 1 and frequency >= A4 - 1:
    print('A4')
elif frequency == B4 + 1 and frequency == B4 - 1:
    print('B4')
else:
    print('The frequency does not match a known note')