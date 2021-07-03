# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:30:06 2021

@author: Alejandro AJ
"""
#Construcción serie  de los meses y agega un elmento al diccionario
import pandas as pd
d = {'Ene':7, 'Feb':5, 'Mar':3}
s = pd.Series(d, index=['Abr','Mar','Feb','Ene'],dtype=int)
print(s)