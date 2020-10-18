import speech_recognition as sr 

r=sr.Recognizer()
while True:
	try:
		with sr.Microphone() as source:
			a=r.listen(source)
		print(r.recognize_google(a))
		if 'bye' in r.recognize_google(a):
			break
			
	except:
		print('error occured ... byee')
		exit(1)


