# Import required packages
import cv2
import pytesseract
  
# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'

#Read image input
front=cv2.imread(r'D:\pthn\text recognition\front.jpg')
back=cv2.imread(r'D:\pthn\text recognition\back.jpg')

#Converting image to string
"""ftxt=pytesseract.image_to_string(front)
btxt=pytesseract.image_to_string(back)

print(ftxt,btxt)
"""
#converting into b&w for more better results
fbw = cv2.cvtColor(front, cv2.COLOR_BGR2GRAY)

#Converting image to string
ftxt=pytesseract.image_to_string(fbw)
#print(ftxt)


#parsing the string read on the front image
x = ftxt.split('\n')

flag=0
no=0
for i in x:
    if "DOB" in i:
        prev=x.index(i)-1
        if x[prev].isspace==True:
            prev=x.index(i)-2
        name=x[prev]
        DOB=i.split(':')
        date=DOB[1].strip()
        nxt=x.index(i)+1
        if x[nxt].isspace() or x[nxt]=='':
            nxt=x.index(i)+2
        g=x[nxt].split('/')
        gender=g[1]
        flag=1
        continue
    if flag==1:
        y=i.split()
        c=0
        for j in y:
            if j.isdigit()==True:
                c+=1
                if c==3:
                    no=str(y[0])+" "+str(y[1])+" "+str(y[2])
                    break
     
            
                

print("Name     : "+name)
print("DOB      : "+date)
print("Gender   : "+gender)
print("card no. : "+no)


#dividing the back image in two parts to extract only english address 
height = back.shape[0]
width = back.shape[1]

width_cutoff = width // 2
#s1 = back[:, :width_cutoff]
s2 = back[:, width_cutoff:]

bbw = cv2.cvtColor(s2, cv2.COLOR_BGR2GRAY)
btxt=pytesseract.image_to_string(bbw)

#print(btxt)

x=btxt.split()

ad=[]
flag=0
for i in range(len(x)):
    if x[i]=="Address:":
        flag=1
        continue
    if flag==1:
        if ' ' not in x[i]:
            ad.append(x[i])
    if len(x[i])==6 and x[i].isdigit():
        break


print("Address  : ",end=' ')
for i in ad:
    print(i,end=' ')















# Read image from which text needs to be extracted
"""img = cv2.imread(r'D:\pthn\text recognition\brnews.png')

text=pytesseract.image_to_string(img)
print(text)

path1=input("Enter the path for the front adhar card image : ")
path2=input("Enter the path for the back adhar card image  : ")

front=cv2.imread(path1)
back=cv2.imread(path2)
"""

"""
front=cv2.imread(r'D:\pthn\text recognition\Scan 02 May 2021_1.jpg')
back=cv2.imread(r'D:\pthn\text recognition\Scan 02 May 2021_2.jpg')

data1=pytesseract.image_to_string(front)
data2=pytesseract.image_to_string(back)
print("2. \n")
print(data1,data2)


front=cv2.imread(r'D:\pthn\text recognition\IMG_20210502_001415.jpg')
back=cv2.imread(r'D:\pthn\text recognition\IMG_20210502_001442.jpg')

data1=pytesseract.image_to_string(front)
data2=pytesseract.image_to_string(back)
print("3. \n")
print(data1,data2)

"""
