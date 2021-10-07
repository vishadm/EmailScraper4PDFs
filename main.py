# import module
from pdf2image import convert_from_path
import pytesseract
import re
import os
# assign directory
directory = 'D:\WORK\python email scraper\exceptions'

# iterate over files in
# that directory
i=0
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
emid=[]
path='D:\WORK\python email scraper'
for pdff in os.listdir(directory):
    f = os.path.join(directory, pdff)
    images=convert_from_path(f,500)
# Store Pdf with convert_from_path function


    for pg in images:

      # Save pages as images in the pdf
        pg.save('page'+ str(i) +'.jpg', 'JPEG')
        i+=1





for img in os.listdir(path):

    im = os.path.join(path, img)
    if im.lower().endswith(('.png','.jpg','.jpeg')):
        resume=pytesseract.image_to_string(im)
        match = re.search(r'[\w\.-]+@[\w\.-]+', resume)
        if match is not None:
            data=match.group(0)
            print(data)


#print(emid)
