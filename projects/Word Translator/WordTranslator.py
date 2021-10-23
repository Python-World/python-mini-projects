from deep_translator import (GoogleTranslator, #importing the deep_translator Libreary and translator API init
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,)

def wordTranslate_google(origin, word):         #Word Translator Using Google API
    translated_word = GoogleTranslator(source = origin, target = 'english').translate(text = word)
    return translated_word

def wordTranslate_myMemory(origin, word):       #Word Translator Using MyMemory
    translated_word = MyMemoryTranslator(source =origin, target='english').translate(word)
    return translated_word

def wordTranslate_lingee(origin, word):         #Word Translator Using Lingee
    translated_word = LingueeTranslator(source = origin, target = 'english').translate(word)
    return translated_word

def wordTranslate_pons(origin, word):           #Word Translator Using PONS
    translated_word = PonsTranslator(source = origin, target = 'english').translate(word)
    return translated_word


def wordTranslate(origin, word): # Word Translator Main Function
    word = word.strip()
    translated_dict = {         #dictionary with the translated words using different API's
        'google': wordTranslate_google(origin, word),
        'myMemory': wordTranslate_myMemory(origin, word),
        #'lingee': wordTranslate_lingee(origin, word),
        'pons': wordTranslate_pons(origin, word)
    }

    translated_word_count = {}  #Creating a blank dictionaries for storing the frequency

    for i in translated_dict.values():  #checking the freequency of the responses
        count = 0
        for j  in translated_dict.values():
            if (i.lower()).strip() == (j.lower()).strip():
                count+=1
            else:
                pass
        if i not in translated_word_count.keys():
            translated_word_count[i] = (count)
        else:
            pass    

    translated_word = ''
    max_count = 0
    for key, value in translated_word_count.items(): #finding the translated word with highest freequency
        
        if max_count < value :
            max_count = value
            if value >= 2: #only select words with atleast freequency of 2
                translated_word = str(key)
            else:
                translated_word = 'NIL'  #storing the translated word
        else:
            pass

    return translated_word, translated_dict, max_count, translated_word_count #returning the translated word