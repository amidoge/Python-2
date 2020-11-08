#new or old style license plate
license_plate = input('What is your license plate number')
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']

if len(license_plate) == 6 and license_plate[0] in alphabet and license_plate[1] in alphabet and license_plate[2] in alphabet and license_plate[3] in numbers and license_plate[4] in numbers and license_plate[5] in numbers:
    print('The characters are valid for an older style license plate')
elif len(license_plate) == 7 and license_plate[0] in numbers and license_plate[1] in numbers and license_plate[2] in numbers and license_plate[3] in numbers and license_plate[4] in alphabet and license_plate[5] in alphabet and license_plate[6] in alphabet:
    print('The characters are valid for an newer style license plate')
else:
    print('License plate is not valid')