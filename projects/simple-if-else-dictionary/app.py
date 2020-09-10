#Simple if else Dictionary.
import json
from difflib import get_close_matches	#if you enter this library will check it.
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(word) == 0:
        return "Please!! Enter word . . . "
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead?\nEnter Y if yes, or N if no : " % get_close_matches(word, data.keys())[0])
        if (yn == "Y") or (yn == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (yn == "N") or (yn == "n"):
            return "Sorry!! The word doesn't exist. Please cross check it.\n"
        else:
            return "We didn't understand your response.\n"
    else:
        return "The word doesn't exist. Please cross check it.\n"

print("Enter word to know meaning!!")
word = input("Enter Word : ")
output = translate(word)
if isinstance(output,list)
    for item in output:
        print(item)
else:
    print(output)
