# -*- coding: utf-8 -*-
"""

@author: sttep
"""

bolsa1 = {
    "Categoria": "Accesorios",
    "Marca": "Guess",
    "Precio": "1,100"
    
    }

bolsa2 = {
    "Categoria": "Accesorios",
    "Marca": "Tommy H",
    "Precio": "1,500"
    
    }


#modificar precio

#print(bolsa1.get("Precio"))

#bolsa1["Precio"] = "1,000"

#print(bolsa1.get("Precio"))


    #bucle for diccionario 2 formas

#for s in bolsa2:
#    print(bolsa2[s])

for s in bolsa2.values():
    print(s)

#con valores
for s, c in bolsa2.items():
    print(s,c)
