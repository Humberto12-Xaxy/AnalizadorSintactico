import string
import re

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

        elif entry[apuntador] == MOVER:
            
            apuntador += 1
            complementoM()

        elif entry[apuntador] == EDITAR:
            
            apuntador += 1
            direccion()
            direccion()
        elif entry[apuntador] == REMOVER:
            
            apuntador += 1
            direccion()
            apuntador += 1
            palabra(entry[apuntador])

        elif entry[apuntador] == CREARA:
            
            apuntador += 1
            direccion()
            apuntador += 1
            palabra(entry[apuntador])
        
        elif entry[apuntador] == MOSTRAR:
            
            apuntador += 1    
            #ls -l PERO
            if entry[apuntador] == '-l': 
                apuntador += 1
                
                if  apuntador == len(entry):
                    n = 'bien'
                
                elif apuntador < len(entry):
                    direccion()
            elif entry[apuntador][0] == DIAGONAL:
                direccion()

        else:
            print('error')
            exit(0)
    else:
        
        if entry[apuntador] == MOSTRAR:
            
            apuntador += 1
            #Ls
            if apuntador == len(entry):
                n = 'bien'
        else:       
        
            print('error')
            exit(0)

def complementoM():
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
                    print('ERROR')
                    exit(0)
        
            palabra(''.join(t))

            if nextStr[apuntadorC] == DIAGONAL:
                complementoM()
            else:
                print('ERROR')
                exit(0)
    
        
    elif string.ascii_letters.__contains__(nextStr[apuntadorC]):
        palabra()

    elif nextStr[apuntadorC] == '.' and nextStr[apuntadorC+1] == '.':
        n = 'Bien'
    else:
        print('error')
        exit(0)

def complementoMO():   
    print()

def direccion():
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
                    print('ERROR')
                    exit(0)
        
            palabra(''.join(t))

            if nextStr[apuntadorC] == DIAGONAL:
                direccion()
            else:
                print('ERROR')
                exit(0)

def sDireccion():
    print()

def palabra(palabra):
    p = re.compile('(\w|_|-)+')

    if p.fullmatch(palabra) is None: 
        print('Error')
        exit(0)


if __name__ == '__main__':
    entry = input('Escribe el comando de linux: ').strip(' ').split()

    comando(entry=entry)
    print('Termino bien')
    # print(string.ascii_letters.__contains__('a'))

