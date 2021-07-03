# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:09:25 2021

@author: Alejandro AJ
"""

import pandas as pd

datos = {'manzanas' : [3,2,0,1], 'naranjas': [0,3,7,2]}
#pasalo al constructor de Pandas DataFrame:
    
datos = pd.DataFrame(datos)
print(datos)