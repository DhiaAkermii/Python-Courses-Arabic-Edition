from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QApplication 


def Rotation(ch):
    res = ""
    for i in range(0,len(ch)):
        res = res + chr(97 + (ord(ch[i]) - 97 + 13) % 26)
    return res

def Miroir(ch):
    return ch[::-1]
   
def Play():
    ch = windows.ch.text()
    if(len(ch)== 0):
        msg = "Veuillez introduire une chaine"
    elif( (len(ch)> 10) or not(ch.islower())):
        msg = "Veuillez introduire une chaine valide !"
    else:
        msg = "La chaine cryptée est : "+Miroir(Rotation(ch))
    windows.res.setText(msg)   

app = QApplication([]) 
windows = loadUi ("InterfaceRotationMiroir.ui") 
windows.show() 
windows.crypter.clicked.connect (Play) 
app.exec_()
