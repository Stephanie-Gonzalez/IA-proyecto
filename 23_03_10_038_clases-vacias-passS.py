# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:00:15 2023

@author: sttep
"""

class Usuarios:
    def __int__(self, name, age):
     self.name = name
     self.age = age

    def muestra_datos(self):
        print("Tu numbre de usuario es:" + self.name, self.age)
        
        
usuario1 = Usuarios ("Memo", 22)

print(usuario1.name, usuario1.age)

del usuario1

print(usuario1.name, usuario1.age)
 