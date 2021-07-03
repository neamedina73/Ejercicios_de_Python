# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:33:04 2021

@author: Alejandro AJ
"""

import pandas as pd
df = pd.DataFrame({
    'play':['john','luigi','javier','alex','richard','leon','camilo'],
    'nro camiseta':[23,78,22,19,45,33,20],
    'edad':['18','22','19','18','17','21','20'],
    'partidos jug':['10','9','11','dc','7','9','6'],
    'goles marcados':[2,0,0,3,2,1,4],
    'faltas':[5,1,0,5,2,2,3]
})
print(df,'\n')
#Serie cuyo indice es el estado, y valor es la cantidad de unicos
print(type(df.groupby('partidos jug')['play'].nunique()),'\n') #nunique, devuelve la serie con el número de observaciones distintas sobre el eje solicitado.
df.groupby('partidos jug')['play'].nunique().plot(kind='bar')(startangle=90,shadow=True, explode=(0.1,0,0,0),autopct='%1.1f%%')
plt.show()
