# Simple_voice_AI

A simple Voice Assistance code you. Must try to execute this code

    #importing essential modules
    
    import datetime
    import speech_recognition as sr
    import pyttsx3
    import wikipedia
    import webbrowser, os, sys, bs4 ,requests
    
    #setup the main engine to work the rest of the  code
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices[1].id)
    engine.setProperty('voice', voices[1].id)

    #Setup the Audio command 
    
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("good morning sir!")
        elif hour>=12 and hour<12:
            speak("Good afternoon sir")
        else:
            speak("Good evening Sir")

        speak("I am Riya")

    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recongnizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n\n")
        except Exception as e:
            speak("Say this again please...")
            return "None"
        return query



    if __name__ == "__main__":
        wishMe()
        speak("I'm Online Boss, What can i do for you")
        while True:
            query = takecommand().lower()


            if 'wikipedia' in query:
                speak("searching on wikipedia....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia ")
                print(f"\n-----{results}-----\n")
                speak(results)
            elif 'play music' in query:
                music_dir = "C:\\Users\\as\\Music\\Videoder"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[1]))


            elif 'open google' in query:
                webbrowser.open('www.google.com')
            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")
            elif 'open facebook' in query:
                webbrowser.open('www.facebook.com')
            elif 'open github' in query:
                webbrowser.open('www.github.com')
            elif 'open instagram' in query:
                webbrowser.open('www.instagram.com')
            elif 'great work' in query:
                speak("thank you Boss")
                
            elif 'bye' or 'good bye', or 'ok bye' or 'exit' or 'quit' in query:
                speak("Good bye Boss. Have a nice Day")



