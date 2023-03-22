n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

if n1 % n2 == 0:
    print('{} é divisível por {}!'.format(n1,n2))
else:
    print('{} não é divisível por {}!'.format(n1,n2))