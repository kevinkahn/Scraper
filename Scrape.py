from bs4 import BeautifulSoup

path = ("C:/Users/kevin/OneDrive/Desktop/Blue Square Asset Management LLC.mhtml")
fh = open(path, "r")
soup = BeautifulSoup(fh.read(), "html.parser")
pathind = [1,1,2,2,1,0,1,0,0,0,0,1,2,0,1,1,1,0]
for ind in pathind:
    soup = soup.contents[ind]
starg = soup
stringlist = [soup.text]
while soup.next_sibling is not None:
    soup = soup.next_sibling
    print('Do append: '+soup.text)
    stringlist.append(soup.text)





