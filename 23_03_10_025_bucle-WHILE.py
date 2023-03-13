# -*- coding: utf-8 -*-
"""

@author: sttep
"""

quote = "Te arremedo lo que escribas:"
quote += "\n Escribe 'salir' para finalizar \n"

mensaje = ""

while mensaje != "salir":
    mensaje = input(quote)
    print(mensaje)