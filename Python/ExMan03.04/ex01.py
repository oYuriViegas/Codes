n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))

if n1 < n2:
    print(f'Os números entre {n1} e {n2} são:')
    for i in range(n1 + 1, n2, 1):
        print(i)
else:
    print(f'Os números entre {n2} e {n1} são:')
    for i in range(n2 + 1, n1, 1):
        print(i)
