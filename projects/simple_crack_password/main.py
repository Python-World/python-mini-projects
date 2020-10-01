import random

##### password #####
PASSWORD="ko6"
###################
result=""
def simple_crack_password ():
    global result
    while result!=PASSWORD :
        result="" 
        for letter in range(len(PASSWORD)):
            list_number=random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
            result="".join(list_number)+str(result)
            print("SEARCH = ",result)
    print(" PASSWORD IS ", result)

simple_crack_password()