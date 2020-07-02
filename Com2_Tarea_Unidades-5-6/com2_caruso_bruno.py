# Com2_Tarea_Unidades-5-6
# Bruno Caruso 
# C-30951-C2

def sustitu_y_cuenta(txtChars,carIn,carOut):
    """Recibe una cadena de caracteres (txtChars), busca en ella coincidencias con un caracter
    que se reciba (carIn), y lo reemplaza con un caracter sustituyente (carOut), finalmente retorna
    la cadena procesada con todos las coincidencias reemplazadas y la cantidad de veces que se realizaron
    los reemplazos."""
    outputStr = ''
    replaceCount = 0
    for char in txtChars:
        if (carIn != carOut):
            if (char == carIn):
                char = carOut
                outputStr += char
                replaceCount += 1
            else:
                outputStr += char
        else:
            outputStr = txtChars 
            return outputStr,replaceCount
    return outputStr,replaceCount

def main():
    """El programa se encarga de reemplazar caracteres en cadenas de texto a traves de una funcion, 
    el mismo devuelve las cadenas originales y las cadenas procesadas, mostrando la cantidad de reemplazos
    en cada caso y la cantidad de reemplazos totales.
    """
    globalReplacements = 0 # Variable para contar reemplazos de palabras totales
    words = [] # Lista de palabras
    carIn = input ('Ingrese un caracter a sustituir: ')
    carOut = input ('Ingrese el caracter sustituyente: ')

    print ('\nIngrese las palabras a procesar de a una por vez (presionando ENTER por cada palabra)\nPara finalizar introduzca "*" como palabra')
    
    while (True): # Recibira infinita cantidad de palabras mientras no se haya ingresado * como palabra (condicion de salida)
        kInput = input()
        if (kInput == '*'):
            break
        else:
            words.append(kInput)

    print ('---------------------------\nResultado:\n')
    for word in words:
        processedWord,replaceCount = sustitu_y_cuenta(word,carIn,carOut)
        globalReplacements += replaceCount
        print (word+' -->> '+processedWord+' - Coincidencias: '+str(replaceCount))
    print ('\nTotal de sustituciones procesadas: '+str(globalReplacements)+'\n')

main()