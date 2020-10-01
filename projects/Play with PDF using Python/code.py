from PyPDF2 import PdfFileReader

# Open the PDF file
pdfFile = open('fileName.pdf', 'rb')

# Create PdfFileReader object to read the file
pdfReader = PdfFileReader(pdfFile)

print("PDF File name: " + str(pdfReader.getDocumentInfo().title))
print("PDF File created by: " + str(pdfReader.getDocumentInfo().creator))
print("- - - - - - - - - - - - - - - - - - - -")

numOfPages = pdfReader.getNumPages()

for i in range(0, numOfPages):
	print("Page Number: " + str(i))
	print("- - - - - - - - - - - - - - - - - - - -")
	pageObj = pdfReader.getPage(i)
	print(pageObj.extractText())
	print("- - - - - - - - - - - - - - - - - - - -")
# Close the PDF file object
pdfFile.close()