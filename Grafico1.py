# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:23:18 2021

@author: Alejandro AJ
"""



import pandas as pd

df = pd.DataFrame({
    'grados':['Sexto','Septimo','Octavo','Noveno','Decimo','Undecimo','Nocturna'],
    'comportamiento':[5.0,5.0,4.5,2.5,3.4,4.6,5.0],
    'nivel':['Secundaria','Secundaria','Secundaria','Secundaria','Media','Media','Adultos'],
    'Salón':['Uno','Dos','Tres','Cuatro','Cinco','Seis','SalonActo'],
    'PromNotas':[2.5, 4.8, 4.3, 3.6,3.1,4.4, 3.2],
    'ProFallas':[12, 0, 7, 6 ,13, 7, 11]
})
print(type(df.groupby('grados')['comportamiento'].nunique()))
df.groupby('grados')['comportamiento'].nunique().plot(kind='pie')
plt.show()