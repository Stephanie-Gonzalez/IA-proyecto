# -*- coding: utf-8 -*-
"""
@author: sttep
"""

def nieve (**kwargs):
    print("El sabor es " + kwargs ["sabor2"] + ".")
    
nieve(sabor1="Fresa", sabor2="Vainilla", sabor3="Chocolate")

#devolver valores

#def suma (s,t):
#    return s + t

#total= suma (7+4)
#print(total)

#mostrar valor llamado

def nieve (sabor="Vainilla"):
    print("El sabor fav es " + sabor)
    
nieve("Fresa") 
nieve()
nieve("Chocolate")
