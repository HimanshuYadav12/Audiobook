import pyttsx3
import PyPDF2
book = open("1.pdf", 'rb') # write the name of your pdf
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(6, pages):  # write the pageno. from where you have to start
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
