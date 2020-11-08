#write a program that reads the sound decibals and then shows what noises can cause that
decibals = int(input('How many decibals do you want us to calculate? '))
jackhammer = 130
gas_lawnmower = 106
alarm_clock = 70
quiet_room = 40
if decibals == jackhammer:
    print('The sound that causes that is a jackhammer.')
elif decibals == gas_lawnmower:
    print('The sound that causes that is a gas lawnmower')
elif decibals == alarm_clock::
    print('The sound that causes that is a alarm clock')
elif decibals == quiet_room:
    print('The sound that causes that is a quiet room')
elif decibals < jackhammer and decibals > gas_lawnmower:
    print('The decibals is in between a jackhammer and a gas lawnmower')
elif decibals < gas_lawnmower and decibals > alarm_clock:
    print('The decibals is in between a gas lawnmower and a alarm clock')
elif decibals < alarm_clock and decibals > quiet_room:
    print('The decibals is in between a alarm clock and a quiet room')
else:
    print('Your input is either too high or too low.')