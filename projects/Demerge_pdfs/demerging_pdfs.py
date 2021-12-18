import PyPDF2

# Note: here instead of Python.pdf you should give the whole path to the pdf if the pdf is not present in the same directory where python program is present
merged_pdf = open('Python.pdf', mode='rb')


pdf = PyPDF2.PdfFileReader(merged_pdf)

(u, ctr, x) = tuple([0]*3)
for i in range(1, pdf.numPages+1):

    if u >= pdf.numPages:
        print("Successfully done!")
        exit(0)
    name = input("Enter the name of the pdf: ")
    ctr = int(input(f"Enter the number of pages for {name}: "))
    u += ctr
    if u > pdf.numPages:
        print('Limit exceeded! ')
        break

    # Note: In the braces you should give the desired path of where new files should be stored
    base_path = '{}.pdf'
    # If you want to store the new pdfs in the same directory, then leave the braces empty
    path = base_path.format(name)
    f = open(path, mode='wb')
    pdf_writer = PyPDF2.PdfFileWriter()

    for j in range(x, x+ctr):
        page = pdf.getPage(j)
        pdf_writer.addPage(page)

    x += ctr

    pdf_writer.write(f)
    f.close()


merged_pdf.close()
print("Successfully done!")
