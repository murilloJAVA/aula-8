valor = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

pDesc = 0 

if valor >= 5000:
        pDesc = 5

if parcelas == 1:
        pDesc = pDesc + 10
        
if parcelas == 2 or parcelas == 3:
        pDesc = pDesc + 5

pDesc = pDesc / 100
valorDesc = valor * pDesc
valorDescformat = "{:.2f}".format(valorDesc)

print(f"Desconto total: {valorDescformat}")

valorFinal = valor - valorDesc
valorFinalformat = "{:.2f}".format(valorFinal)

print(f"Valor final da compra com desconto: {valorFinalformat}")

valorParcela = valorFinal / parcelas
valorParcelaformat = "{:.2f}".format(valorParcela)

print(f"Cada parcela será de: {valorParcelaformat}")

               

    