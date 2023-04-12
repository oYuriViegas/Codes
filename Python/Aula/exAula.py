notas = []
soma = 0

while True:
    valorNota = float(input('Digite a nota: '))
    notas.append(valorNota)
    soma += valorNota
    option = input('Deseja cadastrar outra nota <S/N>:')
    if option == 'S' or option == 's':
        continue
    elif option == 'N' or option == 'n':
        break

tam = len(notas)

for i in range(0, tam):
    if i == 0:
        maiorNota = valorNota
        menorNota = valorNota

    if notas[i] > maiorNota:
        maiorNota = notas[i]

    elif notas[i] < menorNota:
        menorNota = notas[i]

media = soma/ tam

print(f'A média é:{media:.2f}')
print(f'A maior nota é:{maiorNota}')
print(f'A menor nota é:{menorNota}')