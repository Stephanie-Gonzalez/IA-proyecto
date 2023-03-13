# -*- coding: utf-8 -*-
""" 
@author: sttep
"""

#bucle
# x =1 
#whhile x <= 10:
    #print(x)
    #x+=1

# x =1 
# whhile x <= 10:
    #print(x)
    #if x == 5 para brincar este num
         #break  rompe while
    #x+=1

#while se ejecuta entero pero te lo hace saber cuando termina
# x =1 
# whhile x <= 10:
    #print(x)
    #x+=1
#else:
    #print("Saliendo del bucle while...")
   
    
#ejecutar bucle saltando partes

s = 0
while s < 33:
    s += 1
    if s == 4 or s == 11:
        continue
    print(s)