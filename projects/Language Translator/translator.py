from googletrans import Translator

translator = Translator()

language = {"bn": "Bangla",
            "en": "English",
            "ko": "Koren",
            "fr": "French",
            "de": "German",
            "he": "Hebrew",
            "hi": "Hindi",
            "it": "Italian",
            "ja": "Japanese",
            'la': "Latin",
            "ms": "Malay",
            "ne": "Nepali",
            "ru": "Russian",
            "ar": "Arabic",
            "zh": "Chinese",
            "es": "Spanish"
            }

allow = True  # variable to control correct language code input

while allow:  # checking if language code is valid

    user_code = input(
        f"Please input desired language code. To see the language code list enter 'options' \n")

    if user_code == "options":  # showing language options
        print("Code : Language")  # Heading of language option menu
        for i in language.items():
            print(f"{i[0]} => {i[1]}")
        print()  # adding an empty space

    else:  # validating user input
        for lan_code in language.keys():
            if lan_code == user_code:
                print(f"You have selected {language[lan_code]}")
                allow = False
        if allow:
            print("It's not a valid language code!")

while True:  # starting translation loop
    string = input(
        "\nWrite the text you want to translate: \nTo exit the program write 'close'\n")

    if string == "close":  # exit program command
        print(f"\nHave a nice Day!")
        break

    # translating method from googletrans
    translated = translator.translate(string, dest=user_code)

    # printing translation
    print(f"\n{language[user_code]} translation: {translated.text}")
    # printing pronunciation
    print(f"Pronunciation : {translated.pronunciation}")

    for i in language.items():  # checking if the source language is listed on language dict and printing it
        if translated.src == i[0]:
            print(f"Translated from : {i[1]}")
