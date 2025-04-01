sexo = input("Qual seu sexo? ")
peso = float(input("Seu peso atual: "))


def funcao(sexo, peso):
    if sexo == "M" and peso >= 50:
        return True

    elif sexo == "H" and peso >= 60:
        return True

    else:
        return False
    
apto = funcao(sexo, peso)
if apto:
    print("Você está apta para doar sangue!")
else:
    print("Você não está apta para doar sangue!")