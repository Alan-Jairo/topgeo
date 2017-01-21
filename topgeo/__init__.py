""" Esta libreria funciona para realizar calculos topograficos

<topgeo.calcoor("csv")> #Calcula las coordenadas (x,y,z) de un 'csv'.
<topgeo.caldist("csv")> #Calcula las distancias horizontales e inclinadas."""


from coordenada import calcoor
from distancia import caldist
pd.read_csv('Lev_canal.csv')
pd.read_csv('Puntos.csv')
