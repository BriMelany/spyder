# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 10:08:55 2025

@author: DELL
"""

import pandas as pd
import numpy as np
df=pd.read_csv('DatosYT.csv',encoding="latin1")
print(df.dtypes)
print(df.sort_values(by=['xs'],ascending=[True]))
df1=pd.DataFrame(np.sort(df.values,axis=0),index=df.index,columns=df.columns)
print(df1)