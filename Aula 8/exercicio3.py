lista =  []
for i in range(10):
    numero = float(input("Digite um número: "))
    lista.append(numero)
    
maior = float('-inf')
ind = -1

for indice in range(len(lista)):
        if lista[indice] > maior:
              maior = lista[indice]
              ind = indice

print(f"O maior número é: {maior} e seu índice é {ind}")


       
        