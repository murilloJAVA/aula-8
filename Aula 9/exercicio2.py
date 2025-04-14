Votos = [0, 0, 0, 0, 0, 0]

print("0- Para Parar 1- Windows Server 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro")

while True:
    resposta = int(input("Qual o melhor Sistema Operacional para uso em servidores? "))

    if resposta == 0:
        break
    elif resposta < 0 or resposta > 6:
        print("voto inválido. Tente dnv")
        continue

    else:
        if resposta == 1:
            Votos[0] += 1
        if resposta == 2:
            Votos[1] += 1
        if resposta == 3:
            Votos[2] += 1
        if resposta == 4:
            Votos[3] += 1
        if resposta == 5:
            Votos[4] += 1
        if resposta == 6:
            Votos[5] += 1

print(f"{"Sistema Operacional":<25}{"Votos":<8}{"%":<6}")
print(f"{"-" * 20:<25}{"-" * 5:<8}{"-" * 3:<6}")

total = sum(Votos)

print(f"{"Windows Server":<25}{Votos[0]:<8}{Votos[0]/total*100:<6.2f}")
print(f"{"Unix":<25}{Votos[1]:<8}{Votos[0]/total*100:<6.2f}")
print(f"{"Linux":<25}{Votos[2]:<8}{Votos[0]/total*100:<6.2f}")
print(f"{"Netware":<25}{Votos[3]:<8}{Votos[0]/total*100:<6.2f}")
print(f"{"Mac OS":<25}{Votos[4]:<8}{Votos[0]/total*100:<6.2f}")
print(f"{"Outro":<25}{Votos[5]:<8}{Votos[0]/total*100:<6.2f}")



