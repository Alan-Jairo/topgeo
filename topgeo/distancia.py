# Calculo de distancias entre puntos

## Profesor Revisor:
### Dr Ramon Solano Barajas

## Elaborado por:
### Jairo Avalos Velazquez
### Alan Mauricio Cruz Otero


def caldist(lat1, lon1, lat2, lon2):
    """
    Esta funcion sirve para realizar el calculo de distancias entre dos puntos.
    """
    
    # Importamos los modulos numpy y pandas
    import math
    
        rad=math.pi/180
        dlat=lat2-lat1
        dlon=lon2-lon1
        R=6372.795477598
        a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
        distancia=2*R*math.asin(math.sqrt(a))
        return distancia
    caldist(6.27823496943,-75.5694735416,6.28331696378, -75.5689742567)
