import random 
  
print("Number guessing game") 
  
# randint function to generate the  
# random number b/w 1 to 9 
number = random.randint(1, 9) 
  
# number of chances to be given  
# to the user to guess the number  
# or it is the inputs given by user 
# into input box here number of   
# chances are 5 
chances = 0
  
print("Guess a number (between 1 and 9):")  
  
# While loop to count the number 
# of chances 
while chances < 5: 
      
    # Enter a number between 1 to 9  
    guess = int(input()) 
      
    # Compare the user entered number   
    # with the number to be guessed  
    if guess == number: 
          
        # if number entered by user   
        # is same as the generated   
        # number by randint function then   
        # break from loop using loop  
        # control statement "break" 
        print("Congratulation YOU WON!!!") 
        break
          
    # Check if the user entered   
    # number is smaller than   
    # the generated number  
    elif guess < number: 
        print("Your guess was too low: Guess a number higher than", guess) 
  
    # The user entered number is   
    # greater than the generated  
    # number              
    else: 
        print("Your guess was too high: Guess a number lower than", guess) 
          
    # Increase the value of chance by 1 
    chances += 1
          
          
# Check whether the user   
# guessed the correct number  
if not chances < 5: 
    print("YOU LOSE!!! The number is", number)