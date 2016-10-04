from PyPDF2 import PdfFileMerger, PdfFileReader
from urllib2 import Request, urlopen
from StringIO import StringIO
import zipfile

def merge_pdf():
    filenames = ['http://192.168.221.123/desarrollo/020601001000011.pdf','http://192.168.221.123/desarrollo/0206010010000529.pdf']
    merger = PdfFileMerger()

    for filename in filenames:
        remoteFile = urlopen(Request(filename)).read()
        memoryFile = StringIO(remoteFile)
        pdfFile = PdfFileReader(memoryFile)
        merger.append(pdfFile)

    merger.write('hola.pdf')

#merge_pdf()

def zip_files():
    url = 'http://12991301.inei.com.pe'
    filenames_url = ['19290139013.pdf','913091039013.pdf']
    filenames = ['19290139013.pdf','913091039013.pdf']

    for file_url in filenames_url:

    z = zipfile.ZipFile('hola.zip',"w")
    z.write("temp/21902109.pdf")

zip_files()
