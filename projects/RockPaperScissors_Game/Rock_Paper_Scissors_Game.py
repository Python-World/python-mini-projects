import random
print("---------Rock Paper Scissors---------")
while True:
    print("Enter \n 1 for Rock \n 2 for Paper \n 3 for Scissors")
    userchoice = int(input("Enter your choice: "))
    while userchoice > 3 or userchoice < 1 :
        userchoice = int(input("Enter valid input: "))
    choice = ['Rock', 'Paper', 'Scissors']
    print("User choice is " + choice[userchoice - 1])
    botchoice = random.choice(choice)
    print("Bot choice is " + botchoice)
    if choice[userchoice - 1] == botchoice :
        print("It's a tie")
    else :
        if choice[userchoice - 1] == 'Rock' :
            if botchoice == 'Paper' :
                print("Bot wins")
            if botchoice == 'Scissors' :
                print("You wins")
        if choice[userchoice - 1] == 'Paper' :
            if botchoice == 'Rock' :
                print("You wins")
            if botchoice == 'Scissors' :
                print("Bot wins")
        if choice[userchoice - 1] == 'Scissors' :
            if botchoice == 'Paper' :
                print("You win")
            if botchoice == 'Rock' :
                print("Bot win")
    re = input("Press N to quit playing and any other key to continue:  ")
    if re == 'n' or re == 'N' :
        break
print("Thanks for playing")


#END;
