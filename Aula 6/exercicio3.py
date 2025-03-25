linhas = int(input("N linhas: "))
colunas = int(input("N colunas: "))

for l in range (linhas):
    for c in range (colunas):
        if 1 % 2 == 0:
            if c % 2 == 0:
                print("o", end =" ")
            else:
                print("x", end=" ")
        elif 1 % 2 == 1:
            if c % 2 == 0:
                print("x", end=" ")
            else:
                print("o", end=" ") 