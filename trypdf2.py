from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A5,A4,B5 # 可導入不同版型
from reportlab.pdfbase.ttfonts import TTFont    #設定字型之function
pdfmetrics.registerFont(TTFont('bb','C:\Windows\Fonts\kaiu.ttf')) #標楷體
pdfmetrics.registerFont (TTFont ('song', 'C:/Windows/Fonts/msjh.ttc'))  # 註冊字型 通常在c/windows/Fonts中有檔案
import json
import sys
from drawFuc import *

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
        c.showPage()  ##換頁
    elif each == lst[0] :
        print('set size ')   
    elif each[0] == 'Bar' :
        drawBarCode(each[1],each[2],each[3],each[4],each[5],each[6],c)  ##製作條碼
    elif each[0] == 'Line' :
        drawLine(each[1],each[2],each[3],each[4],each[5],c)  ##製作線條
    elif each[0] == 'String' :
        drawLineString(each[1],each[2],each[3],each[4],each[5],c)  ##製作字串
    elif each[0] == 'Image' :
        drawimage(each[1],each[2],each[3],each[4],each[5],c)  ##製作圖片
    else:
        print('類別錯誤')

c.save()
print('otpt : ' + sys.argv[2])