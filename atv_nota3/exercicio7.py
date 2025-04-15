numerosNegativ = []
numerosPositv = []

while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num >= 0:
            numerosNegativ.append(num)
        if num <= 0:
            numerosPositv.append(num)

numeros = numerosPositv + numerosNegativ
print(numeros)