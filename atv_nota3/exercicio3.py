def media(nota1, nota2, nota3, letra):
    if letra == "A":
        mediaA = (nota1 + nota2 + nota3) / 3 
        return  mediaA

    if letra == "P":
        mediaP = ((nota1 * 5 ) + (nota2 * 3) + (nota3 * 2) / (5 + 3 + 2))
        return mediaP
    
