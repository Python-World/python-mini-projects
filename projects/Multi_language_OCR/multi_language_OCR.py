# Author: Acer Zhang
# Datetime: 2021/9/14 
# Copyright belongs to the author.
# Please indicate the source for reprinting.

language = """
Language 	        Abbreviation 		Language 	Abbreviation
Chinese & English 	ch 		            Arabic 	    ar
English 	        en 		            Hindi 	    hi
French 	            fr 		            Uyghur 	    ug
German 	            german 		        Persian 	fa
Japan 	            japan 		        Urdu    	ur
Korean 	            korean 		        Serbian(latin) 	rs_latin
Chinese Traditional 	chinese_cht 	Occitan 	oc
Italian 	        it 		            Marathi 	mr
Spanish 	        es 		            Nepali 	ne
Portuguese 	        pt 		            Serbian(cyrillic) 	rs_cyrillic
Russia 	            ru 		            Bulgarian 	bg
Ukranian 	        uk 		            Estonian 	et
Belarusian 	        be 		            Irish 	ga
Telugu 	            te 		            Croatian 	hr
Saudi Arabia 	    sa 		            Hungarian 	hu
Tamil 	            ta 		            Indonesian 	id
Afrikaans 	        af 		            Icelandic 	is
Azerbaijani 	    az 		            Kurdish 	ku
Bosnian 	        bs 		            Lithuanian 	lt
Czech 	            cs 		            Latvian 	lv
Welsh 	            cy 		            Maori   	mi
Danish 	            da 		            Malay 	    ms
Maltese 	        mt 		            Adyghe 	    ady
Dutch 	            nl 		            Kabardian 	kbd
Norwegian 	        no 		            Avar    	ava
Polish 	            pl 		            Dargwa 	    dar
Romanian 	        ro 		            Ingush  	inh
Slovak 	            sk 		            Lak     	lbe
Slovenian 	        sl 		            Lezghian 	lez
Albanian 	        sq 		            Tabassaran 	tab
Swedish 	        sv 		            Bihari  	bh
Swahili 	        sw 		            Maithili 	mai
Tagalog 	        tl 		            Angika 	    ang
Turkish 	        tr 		            Bhojpuri 	bho
Uzbek 	            uz 		            Magahi  	mah
Vietnamese 	        vi 		            Nagpur  	sck
Mongolian 	        mn 		            Newari  	new
Abaza 	            abq 		        Goan Konkani 	gom
"""

# Import AgentOCR python module
from agentocr import OCRSystem

# Choose OCR language
print(language)
config = input("Please enter the language you want to recognize:")
# Init OCRSystem
ocr = OCRSystem(config=config)
print("OCR system Initialization complete!")

# Start OCR!
while True:
    img = input("Please enter the path where the picture file is located:")
    results = ocr.ocr(img)
    for info in results:
        print(info)