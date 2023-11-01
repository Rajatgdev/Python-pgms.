from PyPDF2 import PdfReader, PdfWriter

n = int(input("enter the number of pages to be read: "))
pdf1 = open("pdf1.pdf", "rb")
pdf2 = open("pdf2.pdf", "rb")

pdf_writer = PdfWriter()

pdf1_reader = PdfReader("pdf1.pdf")
page = pdf1_reader.pages[n - 1]
pdf_writer.add_page(page)

pdf2_reader = PdfReader("pdf2.pdf")
page = pdf2_reader.pages[n - 1]
pdf_writer.add_page(page)

with open("out1.pdf", "wb") as f:
    pdf_writer.write(f)
