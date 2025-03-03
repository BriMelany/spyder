# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 10:08:55 2025

@author: DELL
"""

import pandas as pd
import numpy as np
df=pd.read_csv('canciones.csv',encoding="latin1")
print(df.info())
filas=len(df.index)
print('Filas: ', filas)
df.drop(df.index[filas-1],inplace=True)
filas=len(df.index)
print('Filas: ', filas)