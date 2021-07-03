# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:21:19 2021

@author: Alejandro AJ
"""

import pandas as pd

datos = {'manzanas' : [3,2,0,1], 'naranjas': [0,3,7,2]}
compras = pd.DataFrame(datos, index =['Luis', 'María','José','Carmen'])
print(compras)

#            manzanas  naranjas
#Luis           3         0
#María          2         3
#José           0         7
#Carmen         1         2