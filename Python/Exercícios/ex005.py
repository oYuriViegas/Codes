prova1 = float(input("Insira o valor da prova1: "))
prova2 = float(input("Insira o valor da prova2: "))
peso1 = float(input("Insira o valor do peso1: "))
peso2 = float(input("Insira o valor do peso2: "))

media = float(((prova1*peso1)+(prova2*peso2)/(peso1+peso2)))

print("Média Ponderada = {}".format(media))

if media < 5:
    print('REPROVADO!')
elif media >= 5:
    print('APROVADO!')
elif media >= 8 and media < 9:
    print("“PARABÉNS O DESEMPENHO FOI MUITO BOM")
elif media >=9:
    print("PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR")
