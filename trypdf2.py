from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A5,A4,B5 # 可導入不同版型
from reportlab.pdfbase.ttfonts import TTFont    #設定字型之function
pdfmetrics.registerFont(TTFont('bb','C:\Windows\Fonts\kaiu.ttf')) #標楷體
pdfmetrics.registerFont (TTFont ('song', 'C:/Windows/Fonts/msjh.ttc'))  # 註冊字型 通常在c/windows/Fonts中有檔案
import json
from reportlab.graphics.barcode import code128
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics import renderPDF
import sys
from PIL import Image

def drawLineString(x,y,fnt,sze,strr,file) :  #列印字串
    file.setFont(fnt,sze)
    file.drawString(x,y,strr)
    print('done String')

def drawBarCode(x,y,imgnum,typp,wid,hig,file) : #列印條碼
    if typp =='ean13' :
        barcode_eanbc13 = eanbc.Ean13BarcodeWidget(int(imgnum),barHeight = hig,barWidth  =wid )
        d = Drawing(50, 10)
        d.add(barcode_eanbc13)
        renderPDF.draw(d, file, x, y)
    else :
        barcodexxx = code128.Code128(imgnum,humanReadable=True,barHeight = hig,barWidth = wid )
        barcodexxx.drawOn(file,x,y)
    print('done Barcode')
    
def drawLine(x,y,x2,y2,width,file) :
    file.setLineWidth(width)
    file.line(x,y,x2,y2)
    print('done line')


def drawimage(x,y,x2,y2,image,file) :
    img = Image.open(image)
    w = img.width       
    h = img.height
    wx = x2-x
    hy = y2-y
    if wx/w > hy/h :
        file.drawImage(image,x,y,width=w*hy/h, height=hy)
        print('done image 以高')
    else :
        file.drawImage(image,x,y,width=wx, height=h*wx/w)
        print('done image 以寬')
    




print('start make pdf from ' + sys.argv[1])
with open(sys.argv[1],'r',encoding='utf-8') as f :
    text = f.read()
    lst = json.loads(text)
if type(lst[0]) == str :
    if lst[0] == 'A5' :
        size = A5
    elif lst[0] == 'A4' :
        size = A4
else :
    size = tuple(map(int,lst[0]))
c = Canvas(sys.argv[2],pagesize = size)
for each in lst :
    if each == 'change' :
        c.showPage()
    elif each == lst[0] :
        print('set size ')
    elif each[0] == 'Bar' :
        drawBarCode(each[1],each[2],each[3],each[4],each[5],each[6],c)
    elif each[0] == 'Line' :
        drawLine(each[1],each[2],each[3],each[4],each[5],c)
    elif each[0] == 'String' :
        drawLineString(each[1],each[2],each[3],each[4],each[5],c)
    elif each[0] == 'Image' :
        drawimage(each[1],each[2],each[3],each[4],each[5],c)
    else:
        print('類別錯誤')

c.save()
print('otpt : ' + sys.argv[2])