# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:42:57 2021

@author: Alejandro AJ
"""

import matplotlib.pyplot as plt
valores =[20,40,60,80]

plt.pie(valores, labels=['Rock', 'Balada', 'Ranchera', 'Pop'], colors=['green','yellow','blue','orange']
        , startangle=90,shadow=True, explode=(0.1,0,0,0),autopct='%1.1f%%')
plt.title('Musica')
plt.show()
