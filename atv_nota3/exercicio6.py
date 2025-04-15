def quadrado(number):
    quadrados = []
    for num in range(len(number)):
        numQuadrado = number[num] ** 2
        quadrados.append(numQuadrado)
    return quadrados 