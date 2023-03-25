soma_idades = 0
qnt_idades = 0

while true:
    idade = int(input("Digite a idade (ou zero para encerrar): "))
    if idade == 0:
        break
    soma_idades += idade
    qnt_idades +=1

if qnt_idades > 0:
    idade_media = soma_idades / qnt_idades
    print("A idade média é:", idade_media)
else:
    print("Nenhuma idade foi informada.")