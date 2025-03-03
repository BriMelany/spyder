# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 10:08:55 2025

@author: DELL
"""

import pandas as pd
datos=pd.read_csv('Data.csv',encoding="latin1")
datos.set_index('Location',inplace=True)
print(datos.loc[datos['Court']=='Outdoor',['Surface']])
print(datos.loc[datos['Court']=='Outdoor',['Surface','Winner']])
print('------------------Mas de una condicion------------------')
print(datos.loc[datos['Series'].str.endswith('Slam') & (datos['Surface']=='Clay') & (datos['Winner']=='Federer R.') & (datos['Round']=='The Final') ])