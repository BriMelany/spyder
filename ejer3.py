# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import numpy as np 


datos=pd.read_csv("Data.csv",encoding="latin1")
print(datos.info())
print(datos.iloc[0:20])
print(datos.head())
print(datos.iloc[[0,3,4,5,12],])
print(datos.iloc[[0,3,5,25],[0,5,6]])
print(datos.iloc[:, 0:2])

