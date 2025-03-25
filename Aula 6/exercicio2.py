linhas = int(input("N linhas: "))
colunas = int(input("N colunas: "))

for l in range (linhas):
    for c in range (colunas):
        if l == 0 or l == linhas - 1 or c == 0 or c == colunas - 1:
            print("*", end =" ")

        else: 
            print(" ", end = " ")
    print()
