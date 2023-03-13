# -*- coding: utf-8 -*-
"""

@author: sttep
"""

#diccionarios/objetos

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

#consulta = bolsa1["Marca"], bolsa1["Precio"], bolsa2["Marca"], bolsa2["Precio"]

showBolsas = dict(bolsa1)
print(showBolsas)