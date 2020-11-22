def is_integer(string):
    valid_integer = True
    sign_count = 0
    string = string.strip()
    for char in string:
        if char == ' ':
            break
        else:
            if char in '1234567890': #if the digit is a number then it should be true so far (hopefully until the end)
                valid_integer = True
            elif char in '+-':
                sign_count += 1
                print(sign_count)
                if sign_count > 1: #checking if there is more than one sign
                    valid_integer = False
                    break
            else:
                valid_integer = False
                break
    return valid_integer

a = is_integer('    +-123  ')
print(a)