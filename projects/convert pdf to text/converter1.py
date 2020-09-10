# -*- coding: utf-8 -*-


import PyPDF2


BASEDIR = "C:\Documents\pdf_to_text\output.txt" # This is the sample base directory where all your text files will be stored if you do not give a specific path
txtpath = ""
pdfpath = ""



pdfpath = input("Enter the name of your pdf file - please use backslash when typing in directory path: ")   #Provide the path for your pdf here
txtpath = input("Enter the name of your txt file - please use backslash when typing in directory path: ")   #Provide the path for the output text file  

if(len(txtpath) == 0):
    txtpath = BASEDIR
pdfobj = open(pdfpath, 'rb') 

pdfread = PyPDF2.PdfFileReader(pdfobj)

x = pdfread.numPages


for i in range(x):
    pageObj = pdfread.getPage(i)
    with open(txtpath, 'a+') as f: 
        f.write((pageObj.extractText()))
    print(pageObj.extractText()) #This just provides the overview of what is being added to your output, you can remove it if want
                                    
    
    

pdfobj.close()  


