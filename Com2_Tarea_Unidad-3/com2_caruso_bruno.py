# Bruno Fabrizio Caruso 
# Informática - 1C 2020
# C-30951-C2


def conv_hms_a_seg(h,m,s):
  """Recibe Horas, Minutos, Segundos, realiza las conversiones, 
  y devuelve la totalidad del tiempo expresado en segundos."""
  h = h * 3600 # convierto horas a segundos
  m = m * 60 # convierto minutos a segundos
  output = h+m+s # realizo la sumatoria de todos los segundos
  return output


def conv_seg_a_hms(s):
  """Recibe segundos (s), realiza las conversiones, y 
  devuelve el tiempo expresado en horas,minutos y segundos."""
  m = (s // 60)
  s = (s % 60)
  h = (m // 60)
  m = m % 60
  return h,m,s

def main():
  """Programa principal, se realiza la interaccion con el usuario 
  para que ingrese los datos y finalmente devuelve los mismos procesados."""
  # tiempo 1
  print ("*** Carga del primer tiempo ***")
  print ("[Sistema] Se le solicitara que primero ingrese horas, despues minutos, y finalmente segundos")
  t1_h = int(input("Ingrese la cantidad de horas: "))
  t1_m = int(input("Ingrese la cantidad de minutos: "))
  t1_s = int(input("Ingrese la cantidad de segundos: "))
  t1_inSec = conv_hms_a_seg(t1_h,t1_m,t1_s) # asigno la variable al return de la funcion conv_hms_a_seg

  print ("\n") # separador
 
  # tiempo 2
  print ("*** Carga del segundo tiempo ***")
  print ("[Sistema] Se le solicitara que primero ingrese horas, despues minutos, y finalmente segundos")
  t2_h = int(input("Ingrese la cantidad de horas: "))
  t2_m = int(input("Ingrese la cantidad de minutos: "))
  t2_s = int(input("Ingrese la cantidad de segundos: "))
  t2_inSec = conv_hms_a_seg(t2_h,t2_m,t2_s) # asigno la variable al return de la funcion conv_hms_a_seg

  # sumas de tiempos
  t_inSumSec = (t1_inSec+t2_inSec) # sumo ambos 1
  #tiempos ya convertidos por las funciones en segundos
  t_inHour,t_inMin,t_inSec = conv_seg_a_hms(t_inSumSec) # convierto la suma a horas,minutos,segundos a traves de la funcion


  # tabla 
  print ('\n')
  print ('{0:4^s} {1:4s} {2:4s} {3:8s} {2:4s}'.format('Horas', 'Minutos', 'Segundos', ' '))
  print ('{0:^5d} {1:^7d} {2:^8d} {4:^7s} {3:^8d}'.format(t1_h, t1_m, t1_s, t1_inSec, '======>>'))
  print ('{0:^5d} {1:^7d} {2:^8d} {4:^7s} {3:^8d}'.format(t2_h, t2_m, t2_s, t2_inSec, '======>>'))
  print ('---------------------------------------')
  print ('{0:^5d} {1:^7d} {2:^8d} {4:^7s} {3:^8d}'.format(t_inHour, t_inMin, t_inSec, t_inSumSec, '<<======'))
  print ('\n')

# Llamo a la funcion main para realizar su ejecucion 
main()