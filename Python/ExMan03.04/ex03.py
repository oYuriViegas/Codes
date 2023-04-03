def calcular_media_maior_menor():
    n = int(input("Digite o número de valores que deseja inserir: "))
    soma = 0
    maior_valor = 0
    menor_valor = 0

    for i in range(n):
        valor = float(input(f"Digite o valor {i + 1}: "))
        soma += valor

        if maior_valor == 0 or valor > maior_valor:
            maior_valor = valor
        if menor_valor == 0 or valor < menor_valor:
            menor_valor = valor

    media = soma / n

    print(f"A média dos {n} valores é: {media:.2f}")
    print(f"O maior valor inserido é: {maior_valor}")
    print(f"O menor valor inserido é: {menor_valor}")

calcular_media_maior_menor()