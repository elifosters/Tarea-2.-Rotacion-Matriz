#Elisa Marili Aispuro Aispuro 
#Grupo: 5-3 

import numpy as np

def rot_x(x, y, z, theta):
    '''
    Descripcion
    Rotar las coordenadas en X, multiplicandolas por la matriz rotacion de X
    [ 1, 0         ,  0          ]
    [ 0, cos(theta), -sin(theta) ]
    [ 0, sin(theta),  cos(theta) ]

    Parameters:
        x (float): Valor de coordenada en x
        y (float): Valor de coordenada en y
        z (float): Valor de coordenada en z
        theta (float): valor de el angulo a rotar, que se tiene que pasar a radianes
        matrizTrabajo (numpy.array): Vector de coordenadas para su multiplicación
        matrizRotacion (numpy.array): Matriz necesaria para rotar en X
        vectorResultado (numpy.array): resultado de la rotacion de matriz (p´)

    Returns:
        numpy.array: La matriz rotada en X
    '''
    matrizTrabajo = np.array([x, y, z]) #Pasar las coordenadas a un vector
    theta = np.deg2rad(theta)  #Pasar los grados a radianes.
    matrizRotacion = np.array([[1, 0, 0], [0, np.cos(theta), -(np.sin(theta))], [0, np.sin(theta), np.cos(theta)]])
    vectorResultado = np.dot(matrizTrabajo, matrizRotacion)
    return(vectorResultado)

def rot_y(x, y, z, theta):
    '''
    Descripcion
    Rotar las coordenadas en X, multiplicandolas por la matriz rotacion de X
    [ cos(theta) , 0, sin(theta) ]
    [ 0          , 1, 0          ]
    [ -sin(theta), 0, cos(theta) ]

    Parameters:
        x (float): Valor de coordenada en x
        y (float): Valor de coordenada en y
        z (float): Valor de coordenada en z
        theta (float): valor de el angulo a rotar, que se tiene que pasar a radianes
        matrizTrabajo (numpy.array): Vector de coordenadas para su multiplicación
        matrizRotacion (numpy.array): Matriz necesaria para rotar en y
        vectorResultado (numpy.array): resultado de la rotacion de matriz (p´)

    Returns:
        numpy.array: La matriz rotada en y
    '''
    matrizTrabajo = np.array([x, y, z]) #Pasar las coordenadas a un vector
    theta = np.deg2rad(theta)  #Pasar los grados a radianes.
    matrizRotacion = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-(np.sin(theta)), 0, np.cos(theta)]])
    vectorResultado = np.dot(matrizTrabajo, matrizRotacion)
    return(vectorResultado)

def rot_z(x, y, z, theta):
    '''
    Descripcion
    Rotar las coordenadas en X, multiplicandolas por la matriz rotacion de X
    [ cos(theta), -sin(theta), 0 ]
    [ sin(theta), cos(theta) , 0 ]
    [ 0         , 0          , 1 ]

    Parameters:
        x (float): Valor de coordenada en x
        y (float): Valor de coordenada en y
        z (float): Valor de coordenada en z
        theta (float): valor de el angulo a rotar, que se tiene que pasar a radianes
        matrizTrabajo (numpy.array): Vector de coordenadas para su multiplicación
        matrizRotacion (numpy.array): Matriz necesaria para rotar en z
        vectorResultado (numpy.array): resultado de la rotacion de matriz (p´)

    Returns:
        numpy.array: La matriz rotada en z
    '''
    matrizTrabajo = np.array([x, y, z]) #Pasar las coordenadas a un vector
    theta = np.deg2rad(theta)  #Pasar los grados a radianes.
    matrizRotacion = np.array([[np.cos(theta), -(np.sin(theta)), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    vectorResultado = np.dot(matrizTrabajo, matrizRotacion)
    return(vectorResultado)


def rotar(x, y, z, theta, axis):
    '''
    Descripcion
    Función para determinar la direccion a rotar y llamar a su respectiva función. 

    Parameters:
        x (float): Valor de coordenada en x
        y (float): Valor de coordenada en y
        z (float): Valor de coordenada en z
        theta (float): valor de el angulo a rotar, que se tiene que pasar a radianes
        axis (string): eje de rotacion; puede tomar valor 'x', 'y' o 'z'.

    Returns:
        numpy.array: La matriz rotada en x
        numpy.array: La matriz rotada en y
        numpy.array: La matriz rotada en z
    '''
    if axis == "x" or axis == "X":
        return rot_x(x, y, z, theta)
    if axis == "y" or axis == "Y":
        return rot_y(x, y, z, theta)
    if axis == "z" or axis == "Z":
        return rot_z(x, y, z, theta)



    pass

x = float(input("ingrese el valor de X: "))
y = float(input("ingrese el valor de y: "))
z = float(input("ingrese el valor de z: "))
angulo = float(input("ingrese el valor del angulo: "))
direccion = input("Ingrese la dirección a rotar: ")

print(np.round(rotar(x, y , z, angulo, direccion))) #np.round en caso de tener numeros muy pequeños menores a 0