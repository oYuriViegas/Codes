def tabuada():
    for i in range(0, 11, 1):
        print(f'{n} * {i} = {n*i}')

while True:
    n = int(input('Digite um valor: '))
    tabuada()