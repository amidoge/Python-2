#Capitalize it

string = input("String:")
string_list = []


#itering through the string
for i in range(len(string)):
    #capitalizing first letter
    if i == 0:
        string_list.append(string[i].upper())
    #checking if there is punctuation before the letter.
    elif string[i - 2] in '?.!' and i > 1:
        string_list.append(string[i].upper())
    #if there is an "i" between spaces I want to capitalize it
    elif string[i] == "i" and i != 0 and i != len(string) - 1 and string[i - 1] == ' ' and string[i + 1] == ' ':
        string_list.append(string[i].upper())
    #if there is an "i" with a space behind it, and punctuation next to it, I want to capitalize it.
    elif string[i] == "i" and i != 0 and i != len(string) - 1 and string[i - 1] == ' ' and string[i + 1] in '?,.!':
        string_list.append(string[i].upper())
    #if there is nothing else, then i want to just add the letter
    else:
        string_list.append(string[i])
    
    
#printing the list
for x in string_list:
    print(x, end='')
