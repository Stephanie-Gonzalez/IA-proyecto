# -*- coding: utf-8 -*-
"""

@author: sttep
"""

#input para introducir

tacos=int(input("¿Cuantos tacos de comes?       "))

if tacos <=0:
    print("Registra una cantidad verdadera")
    
    
elif tacos >= 1 and tacos <=10:
    print("Que poquito comes")
    
    
elif tacos <=30:
    print("¿No quieres mas?")
    
else:
    print("Cantidad no valida")