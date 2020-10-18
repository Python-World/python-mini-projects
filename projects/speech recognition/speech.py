import speech_recognition as sr
import webbrowser as wb
r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
with sr.Microphone() as source:
	print('search google | search youtube ')
	print('speak now')
	audio=r3.listen(source)
	print(r3.recognize_google(audio))
if 'video' in r2.recognize_google(audio):
	r2=sr.Recognizer()
	u1='https://www.youtube.com/results?search_query='
	with sr.Microphone() as source1:
		print('enter search query')
		audio1=r2.listen(source1)
		try:
			
			get=r2.recognize_google(audio1)
			print(get)
			wb.get().open_new(u1+get)
		except UnknownValueError:
			print("error")
		
if 'learn' in r2.recognize_google(audio):
	r2=sr.Recognizer()
	u2='https://github.com/'
	with sr.Microphone() as source2:
		print('enter query')
		audio2=r2.listen(source2)
		try:
			get=r2.recognize_google(audio2)
			print(get)
			wb.open_new(u2+get)
		except UnknownValueError:
			print("error")
		
