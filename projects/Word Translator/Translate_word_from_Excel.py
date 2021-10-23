from WordTranslator import *
import pandas as pd

df = pd.read_excel("input.xlsx")

google = []
myMemory = []
lingee = []
pons = []
max_freqency = []
selection = []
selected = []

head = input("Enter the head of the column which contains the words: ")
origin = input("Enter the origin language of the words: ")
target = input("Enter the target language of the words: ")

for word in df[head]:
    translated_word, translated_dict, max_count, translated_word_count = wordTranslate(origin, word, target)
    test_list = []
    selected.append(translated_word)
    for key, value in translated_dict.items():
        if key == 'google':
            google.append(value)
        elif key == 'myMemory':
            myMemory.append(value)
        elif key == 'lingee':
            lingee.append(value)
        elif key == 'pons':
            pons.append(value)
        else:
            pass  
        
        if value == translated_word:
            test_list.append(key)
        else:
            pass
    
    selection.append(test_list)
    max_freqency.append(max_count)   

df['google'] = google
df['myMemory'] = myMemory
df['lingee'] = lingee
df['pons'] = pons
df['Selected Word'] = selected
df['Max Freequency'] = max_freqency

df.to_excel("output.xlsx")