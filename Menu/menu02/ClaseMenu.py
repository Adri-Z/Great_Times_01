#CreadoPo: AIZCH
#Fecha: 09/10/2019
#Asunto: Segunda tarea de la clase del Lunes 7 octubre 2019
#Tarea: Escribir archivo ClaseMenu.py

class ClaseMenu:
    def __init__ (self): # No se incluyen atributos o características para ser guardadas  en una variable.
        self.bienvenida1=" Primer mensaje de bienvenida: Whats up, bro. It is a cool bank" 
    # se lee: 
    # En este objeto de la clase """ClaseMenu""" al aceder al atributo o caraterística bienvenida1,
    # se va a guardar un mensaje, que queda FIJIO. 
    # Entonces, al crear un objeto, solo se le va a pasar el atributo. 
    # Pero el atributo ya viene hecho por default,
    # digamos que el valor que toma es una constante, que en este caso es una cadena de caracteres
    # por lo que a la """función= self.bienvenida1 """ no se le va a asignar nada para guardar en una variable. 
    # Porque el valor ya ha sido asignado.
    
    """
    Duda: En el renglón 15, ¿De qué forma queda bien dicho lo siguiente: ?
    Opción1.- La función self.bienvenida1 siempre resulta un valor constante.
    Opción2.- La función bienvenida1 es constante.
    Creo que la segunda opción notiene tanto sentido, porque solo se puede acceder  al atributo por medio del operador punto.
    """

    #Es como cuando graficamos una funcion constante de R en R, no calculas para cada ´x´ del dominio, el valor ´y´ que va a devolver, porque siempre es el mismo.

        self.bienvenida2="Segunda leyenda para el menú: Excelente día para ingresar a este menú ¡¡ XD !!"
        self.bienvenida3="Leyenda random para usuario: Hola fulanito de tal, porfavor ingrasa tu nomrbe oficial para accedeer a tu cuenta bancaria"
        self.caracteristica4=" Patrocinador oficial ---> ||Laboratorios de ideas geniales|| (Esta es la caraterística del archivo ClaseMenu.py de itzel Z.)"
        self.atributo5="Grandioso mommento para haceer la tarea en Python"

    def bienvenida1(self):
        print(self.bienvenida)
        print("ingrese su nombre")
