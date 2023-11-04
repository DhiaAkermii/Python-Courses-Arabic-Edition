from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QApplication 

def verifier(m,n):
    ch = sorted(m+n) 
    pre = ch[0]
    
    for i in range(1,len(ch)):
        if( (int(ch[i]) - int(pre)) != 1):
            return 0
        pre = ch[i]
    return 1
   
def Play():
    m = windows.M.text()
    n = windows.N.text()
 
    if(int(n) < 0 or int(m) < 0):
        msg = "Veuiller introduire 2 entiers positifs"
    elif(verifier(m,n)):
        msg = n+" et "+ m +" forment une succession parfaite"
    else :
        msg = n+" et "+ m +" ne forment pas une succession parfaite"
   
    windows.resultat.setText(msg)    

app = QApplication([]) 
windows = loadUi ("InterfaceSuccession.ui") 
windows.show() 
windows.verifier.clicked.connect (Play)
app.exec_()

