import PyPDF2
import sys

PDFs = sys.argv[1:]

def pdf_merger(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for file in pdf_list:
		print(file)
		merger.append(file)
	merger.write('/Users/muneeburrehman/Desktop/Projects/PDFs with Python/merged.pdf')

pdf_merger(PDFs)