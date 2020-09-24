import random
from json import load


# function to randomly get one word from words.py and convert the word to uppercase
def get_word():
    with open('words.json') as json_file:
        data = load(json_file)
    wordArray = data["word_list"]
    word = random.choice(wordArray)
    word = word.upper()
    return word


# function to play the game
def play(word):

    # intialise variable
    word_completion = "_" * len(word)  # generate a line to show the number of word
    guessed = False  # indicate the status of guess
    guessed_letters = []  # store guessed letters
    guessed_words = []  # store guessed words
    tries = 6  # user have 6 times of wrong
    # display message and the format of the hangman
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    print("Length of the word: ", len(word))
    print("\n")

    # user can keep guessing when the tries is more than 0 and the answer is not found yet.
    while not guessed and tries > 0:

        # Display message and ask for user input and convert it into uppercase
        guess = input("Please guess a letter or the word: ").upper()

        # check the length of the user input and is it alpha or not
        if len(guess) == 1 and guess.isalpha():

            # display message when user guess the same letter twice
            if guess in guessed_letters:
                print("You already guessed the letter", guess)

            # display message and deduct the tries when user guess the wrong letter
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)

            # dispay message and store the letter when the user guess the correct letter
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)

                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess

                # join the guess word in the word_completion
                word_completion = "".join(word_as_list)

                # if there is not blank space in word_completion change the status of guess to true
                if "_" not in word_completion:
                    guessed = True

        # check the length of the user input and is it alpha or not
        elif len(guess) == len(word) and guess.isalpha():
            # display message when user guess the same letter twice
            if guess in guessed_words:
                print("You already guessed the word", guess)

            # display message and deduct the tries when user guess the wrong letter
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)

            # change the status of guess
            else:
                guessed = True
                word_completion = word

        # display error message for user
        else:
            print("Not a valid guess.")

        # display the format of hangman each time of guess
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        print("Length of the word: ", len(word))
        print("\n")

    # if the variable of guess is true means user win the game
    if guessed:
        print("Congrats, you guessed the word! You win!")
    # else means user lose the game.
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


# function to display the format of hangman
def display_hangman(tries):
    stages = ["""
                    --------
                    |      |
                    |      0
                    |     \\|/
                    |      |
                    |     / \\
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |     \\|/
                    |      |
                    |     / 
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |     \\|/
                    |      |
                    |    
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |     \\|
                    |      |
                    |    
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |      |
                    |      |
                    |    
                    -
              """,
              """
                    --------
                    |      |
                    |      0
                    |      
                    |      
                    |    
                    -
              """,
              """
                    --------
                    |      |
                    |      
                    |      
                    |      
                    |    
                    -
              """
              ]
    return stages[tries]


# main function to start the game
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N): ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
