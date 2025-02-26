# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
datos=pd.read_csv("Data.csv",encoding="latin1")

datos.set_index('Location', inplace=True)
print('---------Melbourne--------')

print(datos.loc['Melbourne'])

print('----Valencia y Houston')

print(datos.loc[['Valencia','Houston']])

print('\n')

print (datos.loc[['Valencia','Houston'],['Series','Court']])

print('------SELECCION POR RANGO-----')

print (datos.loc[['Valencia','Houston'],'Series': 'Round'])

print('------SELECCION POR GRAND SLAM-------')


print(datos.loc[datos['Series'].str.endswith('Slam')])




