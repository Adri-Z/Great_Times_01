#CreadoPor: AIZCH
#Fecha: 04/10/2019
#asunto: Explicando como leer las primeras líneas de un archivo que define a una Clase,
#que después se puede ocupar para crear objetos con Python en el paradigma POO



class PaExplicarLecturaDeCodigo:
  
  def __init__ (self,s,x,winniePooh,w):
    self.saldodememes=s
    self.caracteristicados=x
    self.señorpropietario=winniePooh
    self.mes=w
 
    ############# En POO clase:= {Nombre de la clase U Definición | Definición=(Atributos U Métodos)}
    #### la parabra reservada class indica que voy a dar nombre a una clase
    #### la palabra reservada def indica que voy a dar una definición a continuación
    ############# Hay un concepto que es el de "constructor", el cual tiene un comando asociado,  
    #### y es el comando :  __init__ 
    #### y sirve para: indicar, 2 tipos de COSAS dentro de un parentesis ( __ , __ , __ , __ ) <---
    ############ Tipo de cosa uno
    #### a) una palabra reservada que es el comando: self
    #### y sirve para: indicar que vamos a estar ("creando")/trabajando con objetos
    ############ Tipo de cosa dos
    #### b) EL NOMBRE DE LA VARIABLE que va a guardar el (valor)/(o tipo de dato) de un atributo 
    #### Es decir, ahí no irá el nombre del atributo, aquí más bien va: 
    # Que podrían ser como ejemplos: día, mes, año, carro , cumpleaños
    # O también podrían ser: x, y, z, w, t, s ,d ,f, g, h, i, j, k.
    # El punto es que ahí se a va guardar el valor que yo le entregue al atributo correspondiente a ese lugar.
    ############## HAY una parabra que se coloca inmediatemente de " self."  
    #### y es el nombre de un atributo de la clase.
    #### NOTA: Característeca y Atributo aquí son sinónimos.
    ´´´
    Ejemplo: self.mes = w 
    podría leerse así:
    a) con el operador punto considera a self como un objeto,
    b) es más intercambia la palabra self por la parabra objeto, para leer mejor.
    c) Primero, ve a "la carpeta" objeto. Ósea a la carpeta self.
    c.1) "la carpeta" anterior es una carpeta imaginaria que me inventé para entender mejor.
    c.2) "la carpeta" contiene enlistadas todas las características del objeto
    d) Resulta que Este Objeto que ando contruyendo tiene una característica llamada "mes"
    d) luego con el operador punto, se accede a la característica que se le escribe (o que se le pasa) inmeditamente.
    
    self  ={ es el objeto que estoy construyendo}
      .   ={ que está compuesto por... o que tiene dentro ...}
     mes  ={ una característica que se llama mes}
      =   ={ y a continuación respondo la siguiente pregunta}
          ={ ¿qué valor quiero asignarle a esta característica?}
      w   ={ la respuesta es la variable ´w´}
      ´´´
      
