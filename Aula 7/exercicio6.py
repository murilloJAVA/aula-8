import math

def calculo(n1, n2, n3):
    resultado = n1 ** 0.5 + n2 ** 0.5 + n3 ** 0.5 + (n1 + n2 / 2) + (n2 + n3 / 2) + (n1 + n3 / 2)

    print(f'Resultado: {resultado:.2f}')

calculo(10, 5, 9)