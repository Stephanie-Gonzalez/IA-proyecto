# -*- coding: utf-8 -*-
"""

@author: sttep
"""

#arg arbitrarios

#def alchol(*args):
#    print("El ultimo alchol es  " + args[3] + " Y el primero es " + args [0])
 #   
#alchol("Tequila", "Vodka", "Ron", "Gin")


def alum_profe(profe, sustituto, *args):
    print("Profesor: " + profe)
    print("Susituto: " + sustituto)
    for s in args:
        print("Alumno " + s)
        
lista_alum= ["Ale", "Zara", "Goreti"]

alum_profe("Jesus", "Daniel", *lista_alum)

