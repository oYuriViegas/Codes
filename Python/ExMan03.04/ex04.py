def calcular_fatorial():
    n = int(input("Insira um numero: "))
    fat = 1
    for i in range(1, n + 1):
        fat *= i

    print(f'O fatorial de {n} é {fat}')

while True:
    calcular_fatorial()