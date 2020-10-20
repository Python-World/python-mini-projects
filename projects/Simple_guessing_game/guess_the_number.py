import random

number = random.randint(1,100)
print("guess the number from 1-100")

guess_number = 0

running = True

while running:
    guess = float(input("guess the number: "))
    if guess > number:
        print("your number is too big")
    elif guess < number:
        print("your number is too small")
    elif guess == number:
        running = False
    else:
        print("Invaild Input")
    guess_number += 1






if guess_number == 0:
    guess_number += 1





print("congrats you guessed the number it took you", guess_number, "guesses")