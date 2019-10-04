#CreadoPor: AIZCH
#Fecha: 04/10/2019
#Asunto: Creando la clase Cliente para crear un ejemplo de Banco con POO

class Cliente:

def __init__ (self,n,ide,c,cel):
    self.nombre=n
    self.identificador=ide
    self.correoelectronico=c
    self.numerodecelular= cel

def __str__ (self):
    return "El nombre es: " + str(self.nombre) +"\n"+ "El identificados es: " + str(self.identificador)+"\n"+ "El correo electronico es: " + str(self.correoelectronico)+"El numero de celular es: "+str(self.numerodecelular)
