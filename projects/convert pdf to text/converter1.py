# -*- coding: utf-8 -*-


import PyPDF2
import os


if(os.path.isdir("temp") == False):
    os.mkdir("temp")
    
txtpath = ""
pdfpath = ""



pdfpath = input("Enter the name of your pdf file - please use backslash when typing in directory path: ")   #Provide the path for your pdf here
txtpath = input("Enter the name of your txt file - please use backslash when typing in directory path: ")   #Provide the path for the output text file  

BASEDIR = os.path.realpath("temp") # This is the sample base directory where all your text files will be stored if you do not give a specific path
print(BASEDIR)


if(len(txtpath) == 0):
    txtpath = os.path.join(BASEDIR,os.path.basename(os.path.normpath(pdfpath)).replace(".pdf", "")+".txt")
pdfobj = open(pdfpath, 'rb')

pdfread = PyPDF2.PdfFileReader(pdfobj)

x = pdfread.numPages


for i in range(x):
    pageObj = pdfread.getPage(i)
    with open(txtpath, 'a+') as f: 
        f.write((pageObj.extractText()))
    print(pageObj.extractText()) #This just provides the overview of what is being added to your output, you can remove it if want
                                    
    
    

pdfobj.close()  


