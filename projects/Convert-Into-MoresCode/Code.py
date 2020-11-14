import sys
import pygame
import time

#These are the dots and dashes or dits and dahs correspond to the alphabet

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
        
ONE_UNIT = 0.5
THREE_UNITS = 3 * ONE_UNIT
SEVEN_UNITS = 7 * ONE_UNIT
PATH = 'morse_sound_files/' #The path of the audio file

#The method Verifies that there shouldn't be any special characters
def verify(string):
	keys = CODE.keys()
	for char in string:
		if char.upper() not in keys and char != ' ':
			sys.exit('Error the charcter ' + char + ' cannot be translated to Morse Code')

def main():
    	
	print('Welcome to Alphabet to Morse Code Translator v.01\n')
	
	msg = input('Enter Message: ')
	verify(msg)
	print
	pygame.init()
	fi=[]
	for char in msg:
		if char == ' ':
			print (' '*7,
			time.sleep(SEVEN_UNITS))
		else:
			print (CODE[char.upper()],
			pygame.mixer.music.load(PATH + char.upper() + '_morse_code.ogg'))
			pygame.mixer.music.play()
			time.sleep(THREE_UNITS)
			temp=CODE[char.upper()],pygame.mixer.music.load(PATH + char.upper() + '_morse_code.ogg')
			fi.append(temp)


	actualCode,noneList=zip(*fi) #unzipped the list here into two list to get the final Mores Code at the end 
	
	print("Your Moores Code:",''.join(actualCode))
	print ('\n\nGoodbye!')
	

    	
if __name__ == "__main__":
	main()
