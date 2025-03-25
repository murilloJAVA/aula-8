linhas = int(input("Digite a quantidade de linhas: "))
cont = 1

for i in range(0, linhas):

    for j in range(0, 4):
        if j ==3:
            print("PIM")
            cont += 1
        else: 
            print(cont, end = " ")
            cont += 1