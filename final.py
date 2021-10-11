# import module
from pdf2image import convert_from_path
import pytesseract
import re
import os
import pandas as pd
# assign directory
directory = 'D:\WORK\python email scraper\Data engineer'
df = pd.DataFrame()
pdfname=[]
# iterate over files in
# that directory
i=0
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
emid=[]
path='D:\WORK\python email scraper'
for pdff in os.listdir(directory):
    f = os.path.join(directory, pdff)
    pdfname.append(pdff)
    try:
        images=convert_from_path(f)
    except:
        print("exception in"+ pdff)
        continue
# Store Pdf with convert_from_path function




          # Save pages as images in the pdf
    resume=pytesseract.image_to_string(images[0])
    match = re.search(r'[\w\.-]+@[\w\.-]+', resume)
    if match is not None:
        data=match.group(0)
        print(data)
        emid.append(data)
    else:
        emid.append("email not found")




print(emid)
#excel
columns = ['Emails', 'PDFNames'],
index=['a','b']
df['Emails']=emid
df['PDFNames']=pdfname
df.to_excel('result5.xlsx')
