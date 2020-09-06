import random

def stretch(text,maxlength):
    if len(text) < maxlength:
        randomChar = get_random_char()
        return stretch(text+randomChar,maxlength)
    else:
        return text

def get_random_char():
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?'
    randomChar = chars[random.randint(0,len(chars)-1)]
    return randomChar

while 1:
    try:
        maxlength = int(input(' [?] Enter a length for your password (e for exit): '))
        print("'",stretch('',maxlength),"'\n")
    except:
        if maxlength == 'e':
            break
        print('Please Enter an integer')
