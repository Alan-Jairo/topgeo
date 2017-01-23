# Calculo de Coordenadas (x,y,z)

## Profesor Revisor:
### Dr Ramon Solano Barajas

## Elaborado por:
### Jairo Avalos Velazquez
### Alan Mauricio Cruz Otero


def calcoor(csv):
    """
    Esta es una funcion para realizar el calculo de coordenadas en la biblioteca topgeo.
    """
    
    
     # Agregar los modulos numpy y pandas 
    import numpy as np
    import pandas as pd
    
                                                       
                                                       
    #Almacenamos en la variable pts el archivo csv
    pts = pd.read_csv(csv)
    
    #Se almacenan las variables en las columnas que queremos del csv
    DH = pts['Dist_H']
    AH = pts['Ang_H']
    AV = pts['Ang_V']
    
    #Se crean nuevas columnas en nuestra tabla y se hace el calculo de ellas
    pts ['Pr_x'] = (np.sin(np.radians(AH))* DH)
    pts ['Pr_y'] = (np.cos(np.radians(AH))* DH)
    pts ['Dist_V'] = (np.tan(np.radians(AV))* DH)

    pts.head()
    
    #Se almacenan las nuevas variables en las columnas que queremos de la tabla
    Px = pts['Pr_x']
    Py = pts['Pr_y']
    DV = pts['Dist_V']
    
    # Escribir las coordenadas arbitrarias donde se inicio el levantamiento con Estacion Total(X,Y,Z)
    xx = float(input("Ingresar coordenada arbitraria donde se inicio el levantamiento x: "))
    yy = float(input("Ingresar coordenada arbitraria donde se inicio el levantamiento y: "))
    zz = float(input("Ingresar coordenada arbitraria donde se inicio el levantamiento Z: "))
    
    # Escribir el altura del aparato y altura del prisma
    Alt_A = float(input("Ingresar altura del Aparato Estación Total: "))
    Alt_P = float(input("Ingresar altura del prisma: "))
    
    #Se crean nuevas columnas en nuestra tabla y se hace el calculo de ellas
    pts ['Coo_x'] = (xx + Px)
    pts ['Coo_y'] = (yy + Py)
    pts ['Coo_z'] = (zz + Alt_A + DV - Alt_P)

    pts.head()
    
    x = pts['Coo_x']
    y = pts['Coo_y']
    z = pts['Coo_z']
    
    #Se guarda la tabla terminada con los calculos realizados en un csv
    pts.to_csv('Lev_canal_Terminado.csv')
    
    # Se muestran los datos calculados en el archivo csv se muestran en pantalla
    return pts

calcoor('Lev_canal.csv')
