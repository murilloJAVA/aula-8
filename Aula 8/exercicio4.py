lista =  []

numero_soma = 0

indice_soma = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    lista.append(numero)
    
    if numero % 2 == 0:
        numero_soma = numero + numero_soma 
    
maior = float('-inf')

for indice in range(len(lista)):
    if indice % 2 == 0:
        indice_soma = indice + indice_soma

print(f"Soma de Elementos pares: {numero_soma}")
print(f"Soma dos Índices: {indice_soma}")