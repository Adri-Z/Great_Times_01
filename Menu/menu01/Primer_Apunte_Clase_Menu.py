#CreadoPo: AIZCH
#Fecha: 08/10/2019
#Asunto: Primera tarea de la clase del Lunes 7 octubre 2019
#Tema de la case: Diseñando la Clase Menú.

"""
Nota:  Yo las enlisto claramente, para no perderme en el camino.
 Tarea 1. Escribir el archivo MenuBanco.py
 Tarea 2. Escribir el archivo  Pruebas.py  de esta clase.
 Tarea 3. Traer propuesta pensada para el método "cotejar". Yo le quiero llamar: "cotejarusuario" 
 Tarea 4. Tarea moral. Comparar el código de la profesora (Examen.ParteII) con el nuestro.
"""

######     Apunte de la clase Lunes 7 octubre 2019    #####



###   Primera parte del repaso, de lo que ya deberíamos de saber.

"""
Discusión - Repaso : ¿Qué es un método?


    T o F    :     esValido           (  self       ,     d       ,     m      ,      a                )


 Regresa /         es el nombre          es         ¿Qué parametro va a recibir el método? ¿números, cadenas?
 Responde          nombre del método                ¿Qué necesito para alimentar la función?    

     =                =                  =                             =
 
  Booleanos          La               ( palabra    ,  primer     ,  segundo   ,  tercera                )
                   acción               reservada     atributo      atributo     característica 
                  que realiza           para tra-                                del objeto
                  es validar            bajar con 
                                        objetos

Recordando que son sinónimos las palabras atributo y característica.

En fin, como el método regresa cosas, bueno, una cosa; puedo guardarla en una variable.

dato = esValido(12,4,1998)
Aquí la variable es la palabra dato, y dentro de ella se está guardando el valor que devuelve el método (la acción que realiza el método, valuada en los atributos 12, 4 y 1998) 

La variable llamada dato:
a) La puedo imprimir, simplemente.
b) La puedo meter en una condición  [Es decir, en alguna estructura de control, como if, while, if-elif-elese , etc.]

     En clase se escribió de la siguiente manera lo anterior, para indicar la idea que discutíamos.
     condicion(dato)

     Que bien, podría reescribirse, así, una vez hecha la observación:
     Alguna estructura de control (Variable con un nombre que yo elijo, donde se guarda lo que el método "retornó"/"devolvió"/"retur") ¿Necessariamente debe tener un return?
En este caso, es posible hacer lo anterio, porque el método esValido devuelve valores Booleanos: True / False
"""


###   Segunda parte del repaso, de lo que ya deberíamos de saber.
"""
método print, también se llama salida estandar - {pantalla}
input - entrada estandar - {teclado}
"""
#### Tercera parte 
"""
print("Teclee opción")
opción = input ( "leyenda:" + \n )  
lo guardamos en una variable = {opcion}
invocamos un método = {input}
{se queda esperando a que teclee algo + Enter} = (...esperando para guardar valor en la variable opción...)
Y hasta que doy enter TERMINA la EJECICIÓN. 
"""
####### Ultima parte de la discusión en el salón de clases #########

#Diseño de la clase menú 
#1.- ¿Qué van a decir las leyendas del menú?
#2.- ¿Qué datos va a pedir al usuario?
#3.- ¿Qué métodos va a tener?
#4.- primero esbozamos el funcionamiento del menú, o lo que debería de hacer, y depués vemos cómo escribir la definición como una clase.
 
 ########### Bienvenida al Banco                  }
 ########### Mensaje: ingrese su nombre           } Método: mostrarbienvenida


 ###### <opcion>        } Método: cotejarnombre   ||  Nota: "opción" es una variable doonde se va a guardar el nombre del usuario


 ########### Despliega menú 
 ########### 1. depositar
 ########### 2. retirar
 ########### 3. saldo

"""
Se comentaron dos opciones
A) Un menú donde el usuario ya esté en su cuenta, listo para hacer operaciones
B) Un menú dond el usuario, apenas va a ingresar su nombre para acceder a su cuenta y luego realizar una operación.
"""

 ################ Hasta donde llegamos en el salón de clases: ##############

#MenúBanco.py
class MenuBanco:

    def __init__(self):  #Después del self, no va nada más, porque no recibe más atributos, ¿ Por qué ?
        self.bienvenida="Menú para el usuario, bla, bla, bla" # Personalizar mensaje de bienvenida

    def bienvenida(self):
     print(self.bienvenida)
     print("ingrese su nombre ") 
