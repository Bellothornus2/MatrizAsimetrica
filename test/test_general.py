# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso. 
# Una matriz n*n es antisimetrica si se verifica que 
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i] 
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.

from src.code import es_matriz_antisimetrica
# Casos Test:

def test_simple_correcto():
    matriz = [[0, 1, 2], 
              [-1, 0, 3], 
              [-2, -3, 0]]  
    assert es_matriz_antisimetrica(matriz) == True
#>>> True

def test_simple_correcto2():
    matriz = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    assert es_matriz_antisimetrica(matriz) == True
#>>> True

def test_simple_incorrecto():
    matriz = [[0, 1, 2], 
              [-1, 0, -2], 
              [2, 2,  3]]
    assert es_matriz_antisimetrica(matriz) == False
#>>> False

def test_todo_mal():
    matriz = [[1, 2, 5],
              [0, 1, -9],
              [0, 0, 1]]
    assert es_matriz_antisimetrica(matriz) == False
#>>> False

# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert)




def test_matriz_no_cuadrada():
    matriz4 = [[1,0,0,0],
               [0,1,1,0],
               [0,0,0,1]]
    assert es_matriz_antisimetrica(matriz4) == AssertionError
    #>>>False

def test_matriz_linear():
    matriz5 = [[1,0,0,0,0,0,0,0,0]]

    assert es_matriz_antisimetrica(matriz5) == AssertionError
    #>>>False 