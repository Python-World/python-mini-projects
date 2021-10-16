import random

# ----variables
num = random.randrange(0, 101)
user_num = int()

#-----loop
while num != user_num :
    user_num = int(input("Guess the number(from 0 to 101): "))
    
    # ------conditions
    if user_num == num:
        print("-------------You got it!----------")
        
    elif user_num >  100 :
        print("You have gussed larger number than 100!")
    
    elif user_num > num :
        print("You have gussed a greater number!")

    elif user_num < num :
        print("You have gussed a smaller number!")
