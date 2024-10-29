import pypdf, re
from pypdf import PdfReader
reader = PdfReader("C:\\Users\kevin\OneDrive\Desktop\Blue Square Asset Management LLC.pdf")
page=reader.pages[0]
ex = page.extract_text(0).splitlines()[6:]
info = []
acctpat = re.compile('(^.*?) *((?:Ke|Su).*)')
nampat = re.compile('([a-zA-Z0-9_]*?)((?:\d{1,3}(?:,\d{3})*)?\.\d{2}) ')
for acct in ex:
    p1 = acctpat.split(acct)
    p2 = nampat.split(p1[2])

    #print(p1)
    #print(p2)
    print(f'{p1[1]}  {p2[2]}' )
    #print (p1[1])
    #print(p1[2])
    #print(p2)
    #print (p2[2])
