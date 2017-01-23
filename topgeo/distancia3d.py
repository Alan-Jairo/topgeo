def caldist3d(X1, Y1, Z1, X2, Y2, Z2):
    """
    Esta funcion sirve para realizar el calculo de distancias entre dos puntos arbitrarios.
    """
    # Importamos el modulo numpy
    import numpy as np

    n = (((X1-X2)**2)+((Y1-Y2)**2)+(Z1-Z2))
    Dist = np.sqrt(n)

    return Dist
