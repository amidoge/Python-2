#Ceaser Cipher program (shifts 4 places)
cyphertext = input('Cyphertext: ')
shift = int(input("Shift: "))
plaintext = []

for i in range(len(cyphertext)):
    if cyphertext[i] >= 'A' and cyphertext[i] <= 'Z':
        #convert to ASCII
        ascii_val = ord(cyphertext[i])
        new_letter = ascii_val + shift
        if new_letter > 90:
            new_letter = 64 + (shift - (90 - ascii_val)) #the difference between the original ascii and the max of the uppercase from the start and then add the remaining amount of shifts
        plaintext.append(chr(new_letter))
     
    elif cyphertext[i] >= 'a' and cyphertext[i] <= 'z':
        #convert to ASCII
        ascii_val = ord(cyphertext[i])
        #shifting
        new_letter = ascii_val + shift
        #making sure it doesn't go out to other characters
        if new_letter > 122:
            new_letter = 96 + (shift - (122 - ascii_val)) #the difference between the original ascii and the max of the lowercase from the start and then add the remaining amount of shifts
        plaintext.append(chr(new_letter))
    else: #basically if it is not a letter of any kind
        plaintext.append(cyphertext[i])


print(''.join(plaintext)) #joining the t
