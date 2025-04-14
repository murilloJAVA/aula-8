intervalos = [0,0,0,0]
while True:
    n = int(input("Digite um número positivo ou negativo para sair: "))

    if n < 0:
        break
    elif n <= 25:
        intervalos[0] += 1
    elif 26 <= n <= 50:
        intervalos[1] += 1
    elif 51 <= n <= 75:
        intervalos[2] += 1
    elif 76 <= n <= 100:
        intervalos[3] += 1

print(f"intervalo [0-25]: {intervalos[0]}")
print(f"intervalo [26-50]: {intervalos[1]}")
print(f"intervalo [51-75]: {intervalos[2]}")
print(f"intervalo [76-100]: {intervalos[3]}")