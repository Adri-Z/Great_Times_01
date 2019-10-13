#CreadoPor: AIZCH
#Fecha:13/10/2019
#Asunto: Practica 3 || En Python POO ||
### Creando la Clase PotenciaDeUnNumero

class PotenciaDeUnNumero:
  def __init__ (self,a,b,c):

    self.atributo_base = a
    self.atributo_exponente = b
    self.atributo_respuesta = c

  def __str__ (self):
    return "El numero a= " + str(self.base) + " elevado a la potencia b= " + str(self.exponente)+ " es  calculado con la clasePotencia de un numero  y da "  + str(self.respuesta)
   

   #operacion_cambiar_base_negativa_o_positiva_con_1_o_menos_1 === RENOMBRO === metodo_1_operacion_cambia_signo_base
   #negativo, recibe un numero y lo sustituye por a, pero con el signo contrario
   #negativo recibe un 1 o un menos 1


  def metodo_1_operacion_cambia_signo_base(self,negativo):
    if negativo <0:
      (self.atributo_base) * (-1) = nuevabase
      print (" la nueva base es  "nuevabase"" )
      elif negativo >0:
      (self.atributo_base) * (1) = nuevabase
      print ("La nueva base es  "nuevabase" " )
    else:
      print("Error al  hacer el cambio de signo en la base")
    return (nuevabase) 


# si a = 2
# si b = 3
# si c = desconocido
    def metodo_2_operacion_calcula_potencia_de_a_y_b(self,self.atributo_base,self.atributo_exponente,self.atributo_respuesta)
    exp = self.atributo_exponente + 1
    while i <= exp:
        for x in range(1,exp):
            x = self.atributo_base * self.atributo_base
            print("Se ha calculado el valor pedido")
        else :
            self.atributo_respuesta=x
    return (x)
    
    
