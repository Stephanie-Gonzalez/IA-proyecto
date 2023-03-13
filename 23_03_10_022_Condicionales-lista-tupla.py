# -*- coding: utf-8 -*-
"""

@author: sttep
"""

entrada = input("Introduce el nombre de un avenger:\n")

avengers =  ['capitan america', 'thor', 'black panther', 'blackwidow','hulk']

print('thor' in avengers)

if entrada in avengers:
    print("Tu personaje si es un avenger")
    
else:
    print("El personaje escogigo no es avenger")


