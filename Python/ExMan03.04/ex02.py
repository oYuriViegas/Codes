def calcular_media(n):
    soma = 0
    for i in range(n):
        valor = float(input(f'Digite o valor{i + 1}: '))
        soma += valor
    media = soma / n
    return media


def main():
    n = int(input('Digite o numero de valores que deseja inserir: '))
    print(f'A media dos {n} valores é: {calcular_media(n)}')

while True:
    main()