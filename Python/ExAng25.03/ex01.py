n = int(input("Insira o valor de N(maior ou igual a 10): "))

if n < 10:
    print("N deve ser maior ou igual a 10")
else:
    x = int(input("Digite um numero: "))
    maior = x
    menor = x

    for i in range(1, n):
        x = int(input("Digite um numero: "))
        if x > maior:
            maior = x
        elif x < menor:
            menor = x
    
    print("O maior número é:", maior)
    print("O menor número é:", menor)