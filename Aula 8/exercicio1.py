def lista_numeros(quantidade_numeros):
    lista = []
    for i in range (5):
        valor = int(input('Digite um numero: '))
        lista.append(valor)

    print(lista)
    print(f"O primeiro numero é {lista[0]}")
    print(f"O ultimo numero é {lista[-1]}")