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

if 'runtime' in df.columns:
    df['runtime'] = pd.to_numeric(df['runtime'], errors='coerce')  # Convierte a numérico
    df = df.dropna(subset=['runtime'])  # Elimina NaN

    plt.figure(figsize=(12, 6))
    plt.hist(df['runtime'], bins=range(50, 300, 10), alpha=0.7, color='purple')  # Intervalos de 10 minutos
    plt.xticks(range(50, 300, 20))  # Ajustar etiquetas del eje X
    plt.title('Distribución de la Duración de las Películas')
    plt.xlabel('Duración (minutos)')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

    print(df['runtime'].isnull().sum())  # Cuenta los valores nulos

else:
    print("La columna 'runtime' no está disponible en el dataset.")