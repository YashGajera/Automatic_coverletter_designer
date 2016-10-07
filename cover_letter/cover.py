from PyPDF2 import PdfFileMerger,PdfFileReader,PdfFileWriter
import codecs
  

original_file = PdfFileReader(open("Coverletter_yashgajera_morgan_stanley.pdf",'rb'))
original_page = original_file.getPage(0)
data = original_page.extractText().encode("WinAnsi")
data = " ".join(data.replace(u"\xa0", " ").strip().split())
print data
if "intern" in data:
	print "yes"
else:
	print "no"


 # a writer
pdfWriter=PdfFileWriter()
outfp=open("New_coverletter.pdf",'wb')
pdfWriter.addPage(original_page)

pdfWriter.write(outfp)