#Capitalize it

string = input("String:")
string_list = []


#itering through the string
for i,char in enumerate(string):
    #capitalizing first letter
    if i == 0:
        string_list.append(char.upper())
    #checking if there is punctuation before the letter.
    elif string[i - 2] in '?.!' and i > 1:
        string_list.append(char.upper())
    #if there is an "i" between spaces I want to capitalize it
    elif char == "i" and i != len(string) - 1 and string[i - 1] == ' ' and string[i + 1] == ' ':
        string_list.append(char.upper())
    #if there is an "i" with a space behind it, and punctuation next to it, I want to capitalize it.
    elif char == "i" and i != len(string) - 1 and string[i - 1] == ' ' and string[i + 1] in '?,.!':
        string_list.append(char.upper())
    #if there is nothing else, then i want to just add the letter
    else:
        string_list.append(char)
    
    
#printing the list
print(''.join(string_list))
