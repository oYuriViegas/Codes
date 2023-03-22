import os
def clearTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clearTerminal()
print('=======Conversor Dolar-Real========')
def printOptions():
    print('\nO que deseja fazer?')
    print('\n')
    print('1 - Converter de dolar para real.')
    print('2 - Converter de real para dolar.')
    print('0 - Sair\n')
printOptions()
resp = int(input('Insira uma opção: '))
while resp != 0:
    vr = 0
    vd = 0
    if resp == 1:
        clearTerminal()
        vd = float(input('Insira o valor de dolares para serem convertidos para real: \n'))
        clearTerminal()
        vr = float(vd*5.30)
        print('${:.2f} = R${:.2f}'.format(vd,vr))
    elif resp == 2:
        clearTerminal()
        vr = float(input('Insira o valor de reais para serem convertidos em dolares: \n'))
        clearTerminal()
        vd = float(vr/5.30)
        print('R${:.2f} = ${:.2f}'.format(vr,vd))
    else:
        clearTerminal()
        print('Opção invalida!')
        print('Tente de Novo!')
    printOptions()
    resp = int(input('Insira uma opção: '))
    clearTerminal()
print('Fim!')