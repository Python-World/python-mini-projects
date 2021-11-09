import pyttsx3
from PyDictionary import PyDictionary
import speech_recognition as spr
from gtts import gTTS
import os

#Speaking class
class Speak:
    def SpeakWord(self, audio):
        #Having initial constructor of pyttsx3
        pSpeakEngine= pyttsx3.init('sapi5')
        pVoices= pSpeakEngine.getProperty('voices')

        #Speaking audio that got as parameter
        pSpeakEngine.setProperty('voices', pVoices[0].id)
        pSpeakEngine.say(audio)
        pSpeakEngine.runAndWait()

#Create Recognizer, Microphone instance
sRecog= spr.Recognizer()
sMic= spr.Microphone()

#Capture voice from microphone
with sMic as source:
    print("Speak 'Hello' to initiate Speaking Dictionary!")
    print("----------------------------------------------")

    sRecog.adjust_for_ambient_noise(source, duration= .2)
    rAudio= sRecog.listen(source)

    szHello= sRecog.recognize_google(rAudio, language= 'en-US') 
    szHello= szHello.lower()

#If you said 'Hello', initialize the speaking dictionary
if 'hello' in szHello:
    sSpeak= Speak()
    pDict= PyDictionary()

    print("Which word do you want to find? Please speak slowly.")
    sSpeak.SpeakWord("Which word do you want to find Please speak slowly")
    
    try:
        sRecog2= spr.Recognizer()
        sMic2= spr.Microphone()

        #Capture the word that the user want to find the meaning of 
        with sMic2 as source2:
            sRecog2.adjust_for_ambient_noise(source2, duration= .2)
            rAudio2= sRecog2.listen(source2)
                
            szInput= sRecog2.recognize_google(rAudio2, language= 'en-US')
            
            try:
                #Make sure that the recognizer got the correct word
                print("Did you said "+ szInput+ "? Please answer with yes or no.")
                sSpeak.SpeakWord("Did you said "+ szInput+ "Please answer with yes or no")
                
                sRecog2.adjust_for_ambient_noise(source2, duration= .2)
                rAudioYN= sRecog2.listen(source2)

                szYN= sRecog2.recognize_google(rAudioYN)
                szYN= szYN.lower()

                #If the user said 'yes' (When the recognizer got the correct word)
                if 'yes' in szYN:
                    szMeaning= pDict.meaning(szInput)

                    print("The meaning is ", end="")
                    for i in szMeaning:
                        print(szMeaning[i])
                        sSpeak.SpeakWord("The meaning is"+ str(szMeaning[i]))

                #When the recognizer got the wrong word
                else: sSpeak.SpeakWord("I am sorry Please try again")

            #When the recognizer couldn't understand the answer(yes or no)
            except spr.UnknownValueError: sSpeak.SpeakWord("Unable to understand the input Please try again")
            except spr.RequestError as e: sSpeak.SpeakWord("Unable to provide required output")

    #When the recognizer couldn't understand the word
    except spr.UnknownValueError: sSpeak.SpeakWord("Unable to understand the input Please try again")
    except spr.RequestError as e: sSpeak.SpeakWord("Unable to provide required output")

