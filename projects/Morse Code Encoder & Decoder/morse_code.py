codes = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
}

def encode_text(t):
    encoded_message = ""

    for i in range(len(t)):
        encoded_message += t[i] + ' '
    
    return encoded_message


def decode_morse_code(c):
    decoded_message = ""
    c = c.split(" ")

    for i in range(len(c)):
        for key, value in codes.items():
            if c[i] == value:
                decoded_message += key
    
    return decoded_message



selector = int(input("1-> Encode | 2-> Decode: "))

if(selector == 1):
    print(encode_text(input("Enter text: ").lower()))

else:
    print(decode_morse_code(input("Enter morse code: ")))