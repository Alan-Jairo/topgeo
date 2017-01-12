# Calculo de distancias entre puntos

## Profesor Revisor:
### Dr Ramon Solano Barajas

## Elaborado por:
### Jairo Avalos Velazquez
### Alan Mauricio Cruz Otero


def caldist(csv):
    """
    Esta funcion sirve para realizar el calculo de distancias entre dos puntos.
    """
    
    # Importamos los modulos numpy y pandas
    import numpy as np
    import pandas as pd

    #Almacenamos en la variable pts el archivo csv
    pts = pd.read_csv('Puntos.csv')
    pts.head()

    #Se almacenan las nuevas variables en las columnas que queremos de la tabla
    X = pts['Coor_X']
    Y = pts['Coor_Y']
    Z = pts['Coor_Z']

    # Escribir las coordenadas arbitrarias donde se inicio el levantamiento con Estacion Total(X,Y,Z)
    xx = 100
    yy = 100
    zz = 100

    # Escribir el altura del aparato y altura del prisma
    Alt_A = 1.620
    Alt_P = 1.620

    #Se crean nuevas columnas en nuestra tabla y se hace el calculo de ellas
    n = (((xx-X)**2)+((yy-Y)**2))
    pts ['Dist_H'] = np.sqrt(n)
    pts ['Dist_V'] = (-zz - Alt_A + Alt_P + Z)

    pts.head()

    #Se almacenan las variables en las columnas que queremos del csv
    DH = pts['Dist_H']
    DV = pts['Dist_V']

    # Calculamos la distancia inclinada
    h = ((DH**2)+(DV**2))
    pts ['Dist_I'] = np.sqrt(h)

    pts.head()

    DI = pts['Dist_I']
    #Se guarda la tabla terminada con los clculos realizados en un csv
    pts.to_csv('Puntos_Dist.csv')

    # Se muestran los datos calculados en el archivo csv se muestran en pantalla
    return pts.head()

caldist('Puntos.csv')
