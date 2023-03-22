import os
def clearTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def insertSalary():
    print('\n')
    print('O que deseja fazer?\n')
    print('1 - Calcular salário liquido')
    print('0 - Sair\n')
clearTerminal()
print('========Calcular imposto de renda========')
insertSalary()
resp = int(input('Insira uma opção:'))
clearTerminal()
while resp != 0:
    lv = 0
    if resp == 1:
        value = float(input('Insira o valor do salário bruto: \n'))
        clearTerminal()
        lv = float(value-(value*0.25))
        print('O salário líquido de R${:.2f} é igual a R${:.2f}'.format(value,lv))
    else:
        print('Resposta invalida!')
        print('Tente Novamente!')
    insertSalary()
    resp = int(input('Insira uma opção:'))
    clearTerminal()
clearTerminal()
print('Fim!')
