#Center a string in a terminal

def func(string, width):
    print((width - len(string)) // 2)
    for i in range((width - len(string)) // 2): #integer division so we don't have float error
        print(' ', end='')
    print(string)

func('123456', 100)