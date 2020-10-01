<h1 align = center> OPERATING PDF </h1>

> We are using PyPDF2, we can use the pip package installer.

```
pip install PyPDF2
```
## File Extracting Functions Description
*  We have first used the **open()** method used to open a file in Python for reading, then we will use this file object to initialize the PdfFileReader object.<br/>
*  Once we have the PdfFileReader object ready, we can use its methods like **getDocumentInfo()** to get the file information, or **getNumPages()** to get the total number of pages in the PDF file.<br/>
* Then we have the **getPage()** method to get the page from the PDF file using the page index which starts from 0, and finally the **extractText()** method which is used to extract the text from the PDF file page.
## Contributor ✨

<table>
  <tr>
    <td align="center"><a href="https://github.com/nj1902"><img src="" width="200px;" alt=""/><sub><b>💻 Naman Jain 💻</b></sub></a><br /></td>
   

</table>


Reading the text of the PDF file, which we just did above

Rotating a PDF file page by any defined angle

Merging two or more PDF files at a defined page number.

Appending two or more PDF files, one after another.

Find all the meta information for any PDF file to get informations like creator, author, date of creation, etc.

We can even create a new PDF file using the text coming from some text file.