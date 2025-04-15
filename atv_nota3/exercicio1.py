codigo = int(input("Digite o código do produto:"))
quantidade = int(input("Digite a quantidade do produto:"))

if codigo == 1:
    print(f"Total: R$ {quantidade * 6:.2f}")
elif codigo == 2:
    print(f"Total: R$ {quantidade * 6.5:.2f}")
elif codigo == 3:
    print(f"Total: R$ {quantidade * 5:.2f}")
elif codigo == 4:
    print(f"Total: R$ {quantidade * 3:.2f}")
elif codigo == 5:
    print(f"Total: R$ {quantidade * 2:.2f}")


