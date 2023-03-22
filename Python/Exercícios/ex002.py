import os
def clearTerminal():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')
l1 = int(input('Insira o tamanho de primeiro lado :'))
l2 = int(input('Insira o tamanho de segundo lado :'))
l3 = int(input('Insira o tamanho de terceiro lado :'))

if l1 == l2 == l3:
    print("Triângulo Equilátero")
elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
    print('Triângulo Isócele')
elif l1 != l2 != l3:
    print("Triângulo Escaleno")