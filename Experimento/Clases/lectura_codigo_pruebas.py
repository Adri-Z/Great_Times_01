#CreadoPor: AIZCH
#Fecha: 04/10/2019
#Asunto: Creando la Clase Pruebas para el Banco que estamos construyendo con POO

from Cuenta import *

class Pruebas:
  pass
  print("Algo")
  #Tenía yo, en la clase Cuenta lo siguiente definido
  #(self,s,t,p)  , es decir:
  #(objeto-(por ahora la clase llamada cuenta) con los atributos guardados en este orden, s/saldo, t/tipo, p/propietario)
  ########## Construcción de un objeto arbitrario para la clase Cuenta #########
  # (nombre del ejemplo que voy a construir) := cuenta1
  # (le asigno los siguientes valores) :=    =
  # (Nombre de la clase a la que hago referncia, para construir su objeto) := Cuenta
  # (y luego abro un parentesis para poner los datos adentro como un vector) :=  (  ,   ,  )

  cuenta01=Cuenta(5000,"débito","Jaime R")

  cuenta02=Cuenta(1000,"débito","Roberto D")
  

########### Ahora se sustituyen los datos en la cuenta para crear el  objeto, yo lo visualizo así:
 """
 class Cuenta:
    primera_cuenta = cuenta01
    cuenta01 = (self,50000,debito,Jaime R):
    self.saldo = 50000
    self.tipo = debito
    self.propietario = Jaime R
 Pero para saber de dónde viene este objeto llamado cuenta 1,
 le vamos a poner un apellido, es decir
 le vamos a agregar una palabrita en la "formula" para crear ese objeto, 
 para poder identificar de que clase proviene.
 Quedará así:
 cuenta1 = Cuenta (self , 50000 , debito , Jaime R)
 Luego al ponerle un apellido identificador a la notación, ya no hace falta que ocupemos la palabra self, para decir: "construyeme este objeto",
 entonces, parece conveniente quitar la palabra self de ahí,
 para no estar escribiendo doble,
 por lo que la nomenclatura para la creación del nombre, quedará así:
 cuenta01 = Cuenta ( 50000 , debito , Jaime R )
 """

###### Ahora vamos a leer: 
####  tomar el primer_objeto_de_la_clase = { cuenta01}
####  con el operador punto acceder al siguiente método = { .}
####  el primer método normal de la clase = {depositar}
#### Nota: init y str con métodos especiales de la clase, porque usan palabras reservadas. Con init digo cuales serán los atributos y con str puedo mostrar en cadena los atributos guardados
#### método seguido de unos parenteis para pasarle los valores que recibe mi primer método.

  cuenta01.depositar(5000)
  
  cuenta01.retirar(100)
  
  print(cuenta1)
