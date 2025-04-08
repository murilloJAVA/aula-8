x = int(input("Digite a qntde de numeros: "))

arraylist = []

for i in range(x):
    num = int(input("Digite um numero: "))
    arraylist.append(num)

print(f"Numeros: {arraylist}")

lista_invertida = arraylist[::-1]
print(f"Lista invertida: {lista_invertida}")
