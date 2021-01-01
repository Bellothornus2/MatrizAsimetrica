def sumatorio(n):
    sumador = 0
    for i in range(1,n+1):
        sumador += i
    return sumador

def es_matriz_antisimetrica(matriz):
    try:
        assert len(matriz[0]) == len(matriz) and isinstance(matriz, list) # esto es para que los tests no fallen, si no que funcionen precisamente.
    except AssertionError:
        return AssertionError
    # se debe sumar la n longitud de la matriz con el sumatorio de n, es decir
    #si la longitud de la matriz es 3:
    #3 + 2 + 1
    #si la longitud de la matriz es 4:
    #4 + 3 + 2 + 1
    length_matriz_row = len(matriz)
    acumulator = 0
    answer = None
    base_diagonal = matriz[0][0] #para tener un número de referencia para comparar la diagonal
    for i in range(sumatorio(length_matriz_row)):
        matriz_index = int(i/length_matriz_row) #me ahorro el tener que hacer un bucle dentro de otro con esto, creo que es mas eficiente una division que otro bucle
        cara_normal = matriz[matriz_index][acumulator] #la cara superior derecha de la matriz
        cara_espejo = matriz[acumulator][matriz_index] #la cara inferior izquierda de la matriz
        #si estamos en la diagonal de la matriz y el numero es el mismo o estamos en la "cara normal" de la matriz y su contraparte del espejo es negativa entonces es True
        if matriz_index == acumulator and base_diagonal == cara_normal or matriz_index != acumulator and cara_normal == -cara_espejo:
            answer = True
        #todo lo demás a la hoguera
        else:
            answer = False
            break
        acumulator += 1
        #he pensado que no tiene sentido recorrer la matriz entera, solo la diagonal y la "cara normal" asi que he hecho que el acumulador en ve de recorrer de izquierda
        #a derecha y de arriba a abajo como un pollo sin cabeza, he hecho que recorra la diagonal hasta la derecha y arriba y abajo
        if acumulator == length_matriz_row:
            acumulator = 0 + matriz_index+1
    return answer
    