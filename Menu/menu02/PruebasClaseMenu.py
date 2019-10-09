#CreadoPo: AIZCH
#Fecha: 08/10/2019
#Asunto: Segunda tarea de la clase del Lunes 7 octubre 2019
#Tarea: Escribir archivo de Pruebas.

from ClaseMenu import *
class NombreRandomParaHcerLasPruebas: # Pude haber puesto PruebasClaseMenu, que es el nombre de este archivo.
    pass #Ocupo esta palabra """pass""" porque:
         #En este archivo estoy creando/"Definiendo" una nueva clase, 
         #pero no voy a declarar ningún atributo,
         #ni voy a asignarle nombres ni valores a los objetos que no existirán aquí.
         # Ya que mi intención NO ES declarar definiciones para posibles objetos futuros.
         # Sólo voy a ocupar ésta clase, para que al ejecutar este archivo.py 
         # en la terminal se pueda imprimir (en pantalla) lo que me interesa ver o saber, como:
         # 1) visualizar los objetos que se pueden crear asociados a la clase que definí 
         # (En otros archivos tipo ClaseObjeto1.py, ClaseObjeto2.py, ClaseObjeto3.py, etc.
         #  Cada una con la definición de sus atributos o caraterísticas y con sus métodos.)
         #  y para aplicarles métodos de las clases a dichos objetos.

    print("      ||   Algo , la, la , la.... ji ji ji, jo jo jo.  ||    ")
    print(" ")
    print("Esto es una prueba, para ver cómo funciona la clase ClaseMenu con los 5 atributos que definí en el archivo ClaseMenu.py  XD !!")
    print(" ")

    objeto1=ClaseMenu() # Menciono el objeto que voy a crear, de qué clase va a ser y qué "parametros" le voy a pasar. *No sé si ocupo bien la palabra "parámetros" en este renglón.
    """objeto1"""     # Primero declaro el nombre del objeto que quiero crear.
    """ = """         # Este igual forma parte de la sintáxis, es para especificar que en la palabra anterior voy a guardar los valores que voy a darle al objeto, en la clase que estoy a punto de escribir.
    """ ClaseMenu """ # Se escribe de manera idéntica el nombre de la clase al que quiero acceder / o la clase que quiero ocupar.
    """ () """        # No le paso valores a la función porque no recibe nada.

    # No necesito que se aplique ningún método o que se modifiquen los atributos del objeto (que además ni tiene), por lo que solo voy a imprimirl en pantalla.
    print(objeto1)
