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
    if(len(ch) == 0):
        windows.res.setText("Veuillez introduire une chaine")
    else:
        if( ch.islower()):
            windows.res.setText("La chaine cryptée est : "+Miroir(Rotation(ch)))
        else:
            windows.res.setText("Veuillez introduire une chaine valide !")
app = QApplication([]) 
windows = loadUi ("InterfaceRotationMiroir.ui") 
windows.show()
windows.crypter.clicked.connect (Play) 
app.exec_()
