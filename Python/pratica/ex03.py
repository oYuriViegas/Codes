alunos = {
    'Yuri' : 8,
    'Nina' : 10,
    'Paiva' : 2,
    'Lucas' : 6
}

def calcular_media(notas):
    soma = 0
    quantidade = 0
    for nota in notas.values():
        soma += nota
        quantidade += 1
        
    media = soma / quantidade

    return media

print(calcular_media(alunos))