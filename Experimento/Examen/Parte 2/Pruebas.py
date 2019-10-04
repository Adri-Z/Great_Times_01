#CreadoPor: AIZCH
#Fecha: 04/10/2019
#Asunto: Creando la Clase Pruebas para el Banco que estamos construyendo con POO

from Cuenta import *

class Pruebas:
  pass
  print("Algo")
  
  cuenta1=Cuenta(5000,"débito","Jaime R")
  cuenta2=Cuenta(1000,"débito","Roberto D")
  cuenta1.depositar(5000)
  cuenta1.retirar(100)
  
  print(cuenta1)
