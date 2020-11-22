#Operator Precedence

def precedence(operator):
    if operator in '+-*/^': #checking if it is even an operator
        if operator in '+-':
            return 1
        elif operator in '*/':
            return 2
        else:
            return 3
    else:
        return -1 #This is because the input isn't an operator

if __name__ == '__main__': #This will only work in this file, because this is the __main__. It won't return anything when you import the file function into another file.
    user_input = input("Operator: ")
    function = precedence(user_input)
    if function == -1:
        print('Input from user is not an operator.\nTry again.')
