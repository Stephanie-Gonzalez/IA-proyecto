# -*- coding: utf-8 -*-
"""

@author: sttep
"""

    #ejecutar 10 veces del 0 a 9
# for s in range (19):
#   print (s)


    #se agrega un rango para no mostrar un numero
#for s in range (8,19):
#   print (s)


    #incremento
    
#for s in range (8,20,2):
    #   print (s)
    
    
    #leer y operaciones 
    
#print("lista de numeros:\n")

#numeros = [3,6,9,12,16]

#for s in range(len(numeros)):
    #print("Numero de operacion :", s, "Multiplicacion:", numeros[s], "Resultado: ", numeros[s] * numeros[s])
    
    
#bucle for anidado

ns1 = ["1", "2", "5", "9"]
ns2 = "1" #se genera el 1 en automatico
ns3 = "7"

for s in ns1:
    for c in ns2:
        for e in ns3:
            print(s + c + e)