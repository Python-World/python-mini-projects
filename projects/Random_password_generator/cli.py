from psw import password_generator, PasswordSecurityLevel as PSL
from pyperclip import copy

def main():
    y = 'y'

    print('Hello World !')
    print('Wellcome to password generator')
    print('------------------------------')

    while(True):
        level = input('\n < Enter level of password security > [a/b/c/d/e] : ')
        lenght = int(input(' < Enter lenght of password > : '))
        psw_level = PSL.get(level)

        psw = password_generator(psw_level, lenght)

        print(" < your random passwoed > : ", psw)

        copy_condition = input(
            " would you like to copy it in your clipboard ? [y/n] : ")
        if copy_condition == y:
            copy(psw)
            print(' done!')

        continue_condition = input(" continue ? [y/n] : ")
        if continue_condition != y:
            break

    print('so long.')

if __name__ == '__main__':
    main()
