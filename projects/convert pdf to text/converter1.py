# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:38:39 2020

@author: Admin
"""

import PyPDF2

pdfobj = open('/path/to/pdf', 'rb') #Provide the path for your pdf here

pdfread = PyPDF2.PdfFileReader(pdfobj)

x = pdfread.numPages


for i in range(x):
    pageObj = pdfread.getPage(i)
    with open('/path/to/txt', 'a+') as f: #Provide the path for the output text file
        f.write((pageObj.extractText()))
    print(pageObj.extractText()) #This just provides the overview of what is being added to your output, you can remove it if want
                                    
    
    

pdfobj.close()  