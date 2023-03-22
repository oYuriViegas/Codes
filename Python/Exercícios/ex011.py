n1 = float(input("Insira a nota 1: "))
n2 = float(input("Insira a nota 2: "))
qtdClass = int(input("Insira quantas aulas tiveram: "))
qtdPres = int(input("Insira a quantidade de aulas presentes: "))
freq = int((qtdPres*100)/qtdClass)
media = float((n1+n2)/2)

print("Frequência: {:.2f}%".format(freq))
print("Média: {:.2f}".format(media))

if freq < 75 or media < 4:
    print("REPROVADO!")
elif freq >= 75 and media >= 4 and media < 6:
    print("EXAME!")
elif freq >= 75 and media >= 6:
    print("APROVADO!")

