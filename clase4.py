# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import numpy as np 


datos={'Nombres' : ['Leonardo','Yerson','Briyit','Marian'], 'Calificaciones':['20','15','19','13'],
       'Deportes' : ['Running','Futbol','Natación','Basquet'],'Materias' : [ 'Fabdig','Fisica','Quimica','Biologia']}

df=pd.DataFrame(datos)

print(df)
print('\n'*3)

datos2={'Nombres' : ['N/A','Yerson','Briyit','Marian'], 'Calificaciones':[np.nan,'15','19','13'],
       'Deportes' : ['N/A','Futbol','Natación','Basquet'],'Materias' : [ 'Fabdig','Fisica','Quimica','Biologia']}

df2=pd.DataFrame(datos2)

print(df2)
print('\n'*3)
print(df2.info())
print('\n'*4)

#ESTADISTICASBASICAS
print(df2.describe())
print('\n'*4)
nuevo=pd.DataFrame(datos2)
nuevo=nuevo.replace(np.nan,'0')
print(nuevo)
print('\n'*4)

nuevo['Calificaciones']= nuevo.Calificaciones.astype(int)
print(nuevo.describe())
