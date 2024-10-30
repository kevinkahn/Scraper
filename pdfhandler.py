import os

import re
from pypdf import PdfReader
reader = PdfReader("C:\\Users\kevin\OneDrive\Desktop\Blue Square Asset Management LLC.pdf")
page=reader.pages[0]
ex = page.extract_text(0).splitlines()[6:]
info = []
acctpat = re.compile('(^.*?) *((?:Ke|Su).*)')
nampat = re.compile('([a-zA-Z0-9_]*?)((?:\d{1,3}(?:,\d{3})*)?\.\d{2}) +(\d{1,2}/\d{1,2}/\d{2,4}) +(\d{1,2}/\d{1,2}/\d{2,4}|--)')

with open("C:\\Users\kevin\OneDrive\Desktop\BSVal.csv", "w") as f:
    for acct in ex:
        p1 = acctpat.split(acct)
        p2 = nampat.split(p1[2])
        acctcode = p1[1]
        acctval = p2[2].replace(',','')
        acctdate = p2[3] if p2[4] == '--' else p2[4]
        print(f'{acctcode},{acctval},{acctdate}', file=f)

os.remove("C:\\Users\kevin\OneDrive\Desktop\Blue Square Asset Management LLC.pdf")


