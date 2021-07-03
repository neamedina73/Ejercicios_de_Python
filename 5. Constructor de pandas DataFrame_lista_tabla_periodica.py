# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:49:22 2021

@author: Alejandro AJ
"""

import pandas as pd
elementos = {
    'Número atómico':[1,6,47,88],
    'Masa atómica':[1.088,12.011,107.87,226],
    'Familia':['No metal','No metal','Metal','Metal']
    }
tabla_Periódica = pd.DataFrame(elementos)
print(tabla_Periódica)

#       Número atómico  Masa atómica   Familia
#0               1         1.088      No metal
#1               6        12.011      No metal
#2              47       107.870      Metal
#3              88       226.000      Metal