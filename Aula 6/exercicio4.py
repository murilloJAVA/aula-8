tamanho = int(input("N linhas: "))

for l in range (tamanho):
    for c in range (tamanho):
        if c < l:
            print("$", end =" ")
        elif c >= 1: 
            print("@", end =" ")
    print()

