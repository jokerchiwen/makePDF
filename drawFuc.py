from reportlab.graphics.barcode import code128
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics import renderPDF
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