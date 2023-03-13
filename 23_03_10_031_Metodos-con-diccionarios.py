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


    #eliminar de dos maneras para uno en especif
bolsa1.pop("Marca")
print(bolsa1)

#del bolsa1("Marca")
#print(bolsa1)

    #borrar libreria 
#bolsa1.clear()
#print(bolsa1)

    #añadir categorias

bolsa2["Color"] = "Amarillo"
print(bolsa2)

#bolsa1.update(¨{"Color" : "Azul"})
#print(bolsa1)

    #copia 
    
bolsaCopia = bolsa1.copy()
print(bolsaCopia)

bolsa3 = dict(Cateegoria = "Accesorios",
              Marca = "Westies",
              Precio = "899")

    #valores vacios
    
bolsa4 = ("Categoria", "Marca", "Precio")
vacia = "Valor vacio"

bolsa4 = dict.fromkeys(bolsa4,vacia)

    #busca con if 
    
# if "ID" in bolsa1:
    #print("El producto con ID")
#else
    #print("No existe el ID")

#diccionarios dentro de diccionario

# bolsas = {
# "bolsa12": {
 #   "Categoria": "Accesorios",
  #  "Marca": "Guess",
   # "Precio": "1,100"
    
    #},

# "bolsa2": {
#   "Categoria": "Accesorios",
 #   "Marca": "Tommy H",
  #  "Precio": "1,500"
    # },
   # }
   
   #print(bolsas)






