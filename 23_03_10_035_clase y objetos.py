# -*- coding: utf-8 -*-
"""

@author: sttep
"""

class Nave():
    peso =  5555
    largo = 66
    ancho = 22
    color1 = "Azul"
    color2 = "Amarillo"
    motores = 2
    activada = False
    compuerta_prin = False
    sitema_def = True
    autodestruccion = False
    
    def enciende(self):
        self.activada = True #ecniende nave
        
    def apagar(self):
        self.activada = False

    def abrir_compuerta(self):
        self.compuerta_prin = True
        
    def cerrar_compuerta(self):
        self.compuerta_prin = False
            
    def desactivar_defensas (self):
        self.sistema_def - False

    def activar_defensas (self):
        self.sistema_def - True

    def activar_autodestrucion(self):
        self.autodestruccion = True
        mensaje ="Autodestrucción activada..."
        print (mensaje)
        
    def estado_motores(self):
        if (self.activada):
            return "Motores trabajando al 100%."
        else:
            return "Motores apagados."
    
    def estado_compuerta(self):
        if (self.compuerta_prin):
            return"La compuerta esta abierta"
        else:
            return "La compuerta esta cerrada."

    def estado_defensa(self):
        if (self.sistema_def):
            return "El sistema de defensa esta activado."
        else:
            return "CUIDADO. El sistema de defensa esta descativada"
        
        
    