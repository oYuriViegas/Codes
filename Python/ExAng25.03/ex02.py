qnt = int(input("Insira a quantidade de pessoas: "))

age = int(input("Insira a idade: "))
som = 0
som += age

for i in range(1, qnt):
    if age == 0:
        break
    else:
        age = int(input("Insira a idade: "))
        som += age

media = float(som/qnt)

print("A média das idades é: ", media)
