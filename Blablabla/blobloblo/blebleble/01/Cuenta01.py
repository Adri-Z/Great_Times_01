#CreadoPor: AIZCH
#Fecha: 03/10/2019
#Asunto: Copiando el código que tengo en el cuaderno.

´´´
                                Cuenta
                                
  Atributos:    (sustantivo en minuscula)
                saldo (reales es el tipo de dato / son con punto decimal)
              
  Método:       (verbo en minúscula)
                ¿Qué puedo hacer con una cuenta?
                ¿Qué tiene qué hacer?
                ¿Qué requiere?
                ¿Cuantos valores necesito?
                número de cuenta
                cantidad de dinero
                (en este ejemplo, solo voy a ocupar 1 por el momento, el dinero)
                
                depositar : valor (saldo = saldo + valor)
                
                Mi explicación:
                _"depositar"_ = {Propongo un nombre a una primera función, es decir, al primer método que va a tener mi Futuro objeto cuenta}
                
                Ahora, voy a reescribir lo siguiente a como yo lo entendí:
                f1 = ( y = x + monto )
                
                Donde f1 sería _valor_  = ie = le estoy dando un nombre a mi función ( para que lo lea así la compu)
                      y  sería _saldo_  = ie = le doy un nombrea una función que va a operar de manera iterativa 
                      x + monto = ie = es la regla de correspondencia de la sunción y o la f1
                      
                      Yo entiendo que aquí f1 es el nombre abreviado de todo lo que está entre paréntesis.
                      
   ´´´
  class Cuenta:
  def __init__ (self,s,t,p):
    self.saldo=s
    self.tipo=t
    self.propi=p

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
