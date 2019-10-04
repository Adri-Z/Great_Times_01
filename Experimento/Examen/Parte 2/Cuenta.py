#CreadoPor: AIZCH
#Fecha: 04/10/2019
#Asunto: Crear la clase cuenta para crear un ejemplo de Banco con POO

class Cuenta:
  
  def __init__ (self,s,t,p):
    self.saldo=s
    self.tipo=t
    self.propietario=p
    
  def __str__ (self):
    return "El saldo es: " + str(self.saldo) +"\n"+ "El tipo es: " + str(self.tipo)+"\n"+ "El propietario es: " + str(self.propietario)
  
  def depositar(self,valor):
    if valor>0:
      self.saldo += valor
    else:
      print("Error el valor a depositar es incorrecto")
  
  def retirar(self,valor):
    if valor >0 and valor < self.saldo:
      self.saldo -= valor
    else:
      print("Error el valor a retirar es incorrecto o excede el saldo de la cuenta")
