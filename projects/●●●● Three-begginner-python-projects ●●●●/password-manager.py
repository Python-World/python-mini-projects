#---------Password Manager by Kamalkoranga

data = []

# -----loop
while len(data) < 100 :
    
    # -------inputs
    
    start = input("Add passwwords: \n yes(y)/ no(n) ")
    if start == 'y' :
        name = input("Name: ")
        user_name = input("Username: ")
        user_password = input("Password: ")
        user_data = (name, user_name, user_password)
        data.append(user_data)
        print("-----Saved!------")
        
    elif start == 'n':
        break

# -----Check Password

check_password = input("Want to check password: \n yes(y) no(n) ")
if check_password == 'y' :
    print(data)
else:
    print("|----Okay! Thankyou for using our service----|")
