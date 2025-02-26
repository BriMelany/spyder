# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import numpy as np 


datos=pd.read_csv("Data.csv",encoding="latin1")
print(datos.info())
print(datos.head())
nuevo=pd.DataFrame(datos)
print(nuevo)

nuevo2=nuevo.replace(np.nan,0)
print(nuevo2)

print(nuevo2.describe())
print(nuevo2.describe(include=[np.number]))

nuevo2=nuevo2.replace('N/A','0')
nuevo2=nuevo2.replace('NR','0')
print(nuevo.describe())

nuevo2['Wsets']=nuevo2.Wsets.astype(int)
nuevo2['WRank']=nuevo2.WRank.astype(int)
print(nuevo2.describe())

