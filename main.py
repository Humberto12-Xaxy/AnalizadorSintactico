import string
import re
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from view.mainView import Ui_MainWindow

CREAR = 'mkdir'
MOVER = 'cd'
MOSTRAR = 'ls'
EDITAR = 'mv'
REMOVER = 'rm'
CREARA = 'touch'
DIAGONAL = '/'

apuntador = 0
apuntadorC = 0

def comando(entry):

    global apuntador

    if len(entry)!=1:

        if entry[apuntador] == CREAR:
        
            apuntador += 1

            palabra(entry[apuntador])

            return 'Correcto'

        elif entry[apuntador] == MOVER:
            
            apuntador += 1
            complementoM(entry)

            return 'Correcto a'

        elif entry[apuntador] == EDITAR:
            
            apuntador += 1
            direccion(entry)
            direccion(entry)

            return 'Correcto'

        elif entry[apuntador] == REMOVER:
            
            apuntador += 1
            direccion(entry)
            apuntador += 1
            palabra(entry[apuntador])

            return 'Correcto'

        elif entry[apuntador] == CREARA:
            
            apuntador += 1
            direccion(entry)
            apuntador += 1
            palabra(entry[apuntador])

            return 'Correcto'
        
        elif entry[apuntador] == MOSTRAR:
            
            apuntador += 1    
            #ls -l PERO
            if entry[apuntador] == '-l': 
                apuntador += 1
                
                if  apuntador == len(entry):
                    return 'Correcto'
                
                elif apuntador < len(entry):
                    direccion(entry)
                    return 'Correcto'
            elif entry[apuntador][0] == DIAGONAL:
                direccion(entry)
                return 'Correcto'

        else:
            return 'Error'
    else:
        
        if entry[apuntador] == MOSTRAR:
            
            apuntador += 1
            #Ls
            if apuntador == len(entry):
               return 'Correcto'
        else:       
        
            return 'Error'
def complementoM(entry):
    global apuntadorC
    nextStr = entry[apuntador]
    
    if nextStr[apuntadorC] == DIAGONAL:
        if apuntadorC+1 < len(nextStr):
            apuntadorC += 1
            t = []
            while nextStr[apuntadorC] != DIAGONAL:
                if apuntadorC+1 < len(nextStr):
                    t.append(nextStr[apuntadorC])
                    apuntadorC += 1
                else:
                    return 'Error'
        
            palabra(''.join(t))

            print(nextStr[apuntadorC])
            if nextStr[apuntadorC] == DIAGONAL:
                complementoM(entry)
            else:
                print('entré')
                return 'Error'
    
        
    elif string.ascii_letters.__contains__(nextStr[apuntadorC]):
        palabra(nextStr)

    elif nextStr[apuntadorC] == '.' and nextStr[apuntadorC+1] == '.':
        return 'Correcto'
    else:
        return 'Error'

def direccion(entry):
    global apuntadorC
    nextStr = entry[apuntador]

    if nextStr[apuntadorC] == DIAGONAL:
        if apuntadorC+1 < len(nextStr):
            apuntadorC += 1
            t = []
            while nextStr[apuntadorC] != DIAGONAL:
                if apuntadorC+1 < len(nextStr):
                    t.append(nextStr[apuntadorC])
                    apuntadorC += 1
                else:
                    return 'Error'
        
            palabra(''.join(t))
               
            if nextStr[apuntadorC] == DIAGONAL:
                direccion(entry) 
            else:
                return 'Error'


def palabra(palabra):
    p = re.compile('(\w|_|-)+')

    if p.fullmatch(palabra) is None: 
        return 'Error'
    else:
        return 'Correcto'
class main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.comprobacion)
    
    def comprobacion(self):
        entry = self.ui.lineEdit.text().strip(' ').split()
        response = comando(entry= entry)

        self.ui.message.setText(response)
        print('Termino bien')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())
    # entry = input('Escribe el comando de linux: ').strip(' ').split()

    # comando(entry=entry)
    # print('Termino bien')

    # print(string.ascii_letters.__contains__('a'))

