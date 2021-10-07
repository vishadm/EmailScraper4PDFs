import PyPDF2
import re
import pandas as pd
import os
data = []

for filename in os.listdir('/content/drive/MyDrive/RESUME/'):
    if filename.endswith("pdf"):
        # Your code comes here such as

       data.append(filename)
emids=[]
path='/content/drive/MyDrive/RESUME/'
for i in data:
    file=path+i
    pdff=open(file,'rb')

    pdread=PyPDF2.PdfFileReader(pdff)
    pdobj=pdread.getPage(0)
    txt=pdobj.extractText()

    #regex email finder
    match = re.search(r'[\w\.-]+@[\w\.-]+', txt)
    emids.append(match.group(0))

df = pd.DataFrame()
df['Emails'] = emids
df.to_excel('result.xlsx', index = False)
