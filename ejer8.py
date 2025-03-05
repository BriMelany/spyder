# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 22:21:27 2025

@author: DELL
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('MoviesDataset.csv',encoding="latin1")
print(df.info())

if 'release_date' in df.columns and 'revenue' in df.columns :
    df['release_date']=pd.to_datetime(df['release_date'],errors='coerce')
    df['year']=df['release_date'].dt.year
    print(df['year'])
    plt.figure(figsize=(10, 6))
    df.groupby('year')["revenue"].sum().plot(kind='line', marker= 'o', color='red')
    plt.title('Ingresos por Año')
    plt.xlabel('Año')
    plt.ylabel('Ingresos (en millones)')
    plt.grid(True)
    plt.show()
else:
    print('Columnas no existen')