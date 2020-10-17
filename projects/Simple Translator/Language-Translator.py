#importing Translator from googletrans.
from googletrans import Translator

#giving the input sentence which need to be translated.
sentence = str(input("Enter the sentence:"));

#assigning the Translator() to a variable translator.
translator = Translator();

#translating a sentence from one language to another.
# src = "Input sentence in one language"
# dest = "To which language to be changed"
translated_sentence = translator.translate(sentence,src='en',dest='ml');   # here 'en' is English and 'ml' is 'Malayalam'

#to print the translated sentence.
print(translated_sentence.text);
