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
while True:

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
        print(
            f'CONGRATULATIONS! YOU HAVE GUESSED THE \
            NUMBER {number} IN {chances} ATTEMPTS!')
        # Printing final statement using the f-strings method;
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
    
