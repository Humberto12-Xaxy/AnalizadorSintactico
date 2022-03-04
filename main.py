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
            if complementoM(entry) == 'Error':
                return 'Error'
            else:
                return 'Correcto'

        elif entry[apuntador] == EDITAR:
            
            apuntador += 1
            # verificar

            response1 = direccion(entry)
            response2 = direccion(entry)

            print(response1)
            print(response2)
            if response1 is None and response2 is None:
                return 'Correcto'
            elif response1 is None and response2 == 'Error':
                return 'Error'
            elif response1 == 'Error' and response2 == 'Error':
                return 'Error'

        elif entry[apuntador] == REMOVER:
            
            #error index out of range
            apuntador += 1
            responseD = direccion(entry) 
            apuntador += 1
            responseP = palabra(entry[apuntador])

            
            if responseD is None and responseP == 'Correcto':
                return 'Correcto'
            else: 
                return 'Error'

        elif entry[apuntador] == CREARA:
            
            apuntador += 1
            responseD = direccion(entry)
            apuntador += 1
            responseP = palabra(entry[apuntador])

            if responseD is None and responseP == 'Correcto':
                return 'Correcto'
            else: 
                return 'Error'
        
        elif entry[apuntador] == MOSTRAR:
            
            apuntador += 1    
            #ls -l PERO
            if entry[apuntador] == '-l': 
                apuntador += 1
                
                if  apuntador == len(entry):
                    return 'Correcto'
                
                elif apuntador < len(entry):
                    responseD = direccion(entry)
                    if responseD is None:
                        return 'Correcto'
                    else:
                        return 'Error'
            elif entry[apuntador][0] == DIAGONAL:
                responseD = direccion(entry)
                if responseD is None:
                    return 'Correcto'
                else:
                    return 'Error'

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
    print(apuntadorC)
    print(len(entry))
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
                if complementoM(entry) != 'Error':
                    complementoM(entry)
                else:
                    return 'Error'
            else:
                return 'Error'
    
        
    elif string.ascii_letters.__contains__(nextStr[apuntadorC]):
        palabra(nextStr)

    elif nextStr[apuntadorC] == '.' and len(nextStr)==1:
        return 'Error'
        
    elif nextStr[apuntadorC] == '.' and nextStr[apuntadorC+1] == '.':
        return 'Correcto'
    else:
        return 'Error'

def direccion(entry):
    global apuntadorC
    nextStr = entry[apuntador]

    print(apuntador)
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
                if direccion(entry) != 'Error':
                    direccion(entry)
                else:
                    return 'Error'
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

