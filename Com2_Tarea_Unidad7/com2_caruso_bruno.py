# Com2_Tarea_Unidad-7
# Bruno Caruso 
# C-30951-C2

def agrega_nombres (tup_tuplas, lis_cad):
    """Esta funcion recorre los elementos de la tupla recibida,
    comprueba que los elementos que no esten en la lista recib-
    ida sean agregados y retorna la cantidad de incorporaciones
    que se realizaron."""
    incorporaciones = 0
    for posTupla in range(0,len(tup_tuplas)): # Recorre la tupla
        if not (tup_tuplas[posTupla][0] in lis_cad): # Comprueba si el elemento no existe en la lista
            lis_cad.append(tup_tuplas[posTupla][0]) # Si no existe, lo incorpora a la lista del programa principal
            incorporaciones += 1 # Suma una nueva incorporacion
    return incorporaciones # Retorna la cantidad de incorporaciones totales


def main():
    """Este programa declara 2 variables, una tupla de tuplas y una lista de cadenas de caracteres, muestra 
    su estado por pantalla y despues llama a la funcion agrega_nombres pasando la tupla y la lista como pa-
    rametros. Aquella funcion le devuelve la cantidad de incorporaciones que son mostradas al final junto 
    con los nuevos estados de las variables con las modificaciones ya hechas."""

    tupla = (('Esteban', 'Kero') , ('Enrique', 'Cido') , ('Sara', 'Ampión') , ('Ana', 'Lista'))
    lista = [ 'Luisa', 'Enrique', 'Hugo', 'Esteban' ]

    print ("\nEstado actual de las variables:\n")
    print ("tupla = ", tupla, "\nlista = ", lista)

    print ('\n--------------------------------\n')
    incorp = agrega_nombres (tupla, lista)

    print ("Nuevo estado de las variables:\n")
    print ("tupla = ", tupla, "\nlista = ", lista)
    print ("\n* Se realizaron ",incorp," incorporaciones.\n")
    
main()