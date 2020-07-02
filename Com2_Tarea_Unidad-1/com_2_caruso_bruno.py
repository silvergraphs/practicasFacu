# Bruno Fabrizio Caruso 
# Informática - 1C 2020
# C-30951-C2


def tablaNatural(n):
  for x in range(0, n+1):
    output = print(n ," x ", x, " = ", x*n)
  return output

def calcular():
  n = int(input("Ingrese un numero natural: "))
  tablaNatural(n)
  preg = input ("Desea volver a calcular otra tabla? S/N\n")
  if preg=="S" or preg=="s":
    calcular()
  elif preg=="N" or preg=="n":
    pass
    
calcular()
