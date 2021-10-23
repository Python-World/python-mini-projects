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