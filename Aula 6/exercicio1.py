x = int(input("Digite a quantidade de numeros a serem testados: "))

primos = 0
for i in range(x):
    n = int(input("Digite o numero a ser testado: "))
    if n > 1 and n % 1 == 0:
        eh_primo = True
        for j in range (2, n):
            if n % j == 0:
                eh_primo = False

    else:
        primos = primos + 1
        print(f"O numero {n} é primo")
print(f"A quantidade de numeros primos é {primos}")
