# -*- coding: utf-8 -*-
"""

@author: sttep
"""

print("Bonjour chef, ¿Que alimento desea comprar?\n\n" +
      "Ingredientes disponibles:\n\n" +
      "Vegetales: \n\n" +
      "1-Papa: 30 monedas.\n" +
      "2-Zanahoria: 35 monedas. \n" +
      "3-Brocoli: 40 monedas\n\n" +
      
      "Proteina: \n\n" +
      "4- Pescado: 60 monedas\n"
      "5- Carne de res: 75 monedas \n\n")

comprar = [4]

dinero = 300

papa = 30

zanahoria = 35

brocoli = 40

pescado = 60

res = 75

if 0 in comprar or comprar == []:
    print("Especifica un numero entre 1 y 5")
    
if 1 in comprar:
    dinero = dinero - papa
    
if 2 in comprar:
    dinero = dinero - zanahoria 
            
if 3 in comprar:
    dinero = dinero - brocoli 
               
if 4 in comprar:
    dinero = dinero - pescado 
                      
if 5 in comprar:
    dinero = dinero - res
    
else:
    print("numero no valido, verificalo")
    
if dinero < 0:
    print("Oops te haz pasado del presupuesto")
    
if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4] or comprar == [5]:
    print("Te quedan " + str(dinero) + "Monedas")
    print("Se añadieron el/los ingredientes a la canasta")


















                             