# -*- coding: utf-8 -*-
"""

@author: sttep
"""

class Agentes():
    
    def __init__(self, name, pin):
        self.name=name
        self.pin=pin

    def saludo(self):
        print("Saludos " + self.name + ". Iniciaste sesion correctamente.")


    def despedida (self):
        print (self.name + ", cerraste sesion."

usu1 = Agentes("Cesar", "5555")    
        
us2=Agentes("Jaime", "8115")

us1.saludo()
us1.saludo()