import os
def clearTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def printOptions():
    print('\nO que deseja fazer?')
    print('\n')
    print('1 - Converter Fahrenheit.')
    print('2 - Converter Kelvin.')
    print('3 - Converter Rankine.')
    print('4 - Converter Réaumur.')
    print('0 - Sair\n')
clearTerminal()
printOptions()
resp = int(input('Insira uma opção: '))
while resp != 0:
    clearTerminal()
    if resp == 1:
        Fahrenheit = float(input("Insira um valor: "))
        clearTerminal()
        Celsius = float((5*(Fahrenheit-32))/9)
        print("{:.2f} Fahrenheit é igual a {:.2f} Celsius.".format(Fahrenheit, Celsius))
        os.system("pause")
    elif resp == 2:
        Kelvin = float(input("Insira um valor: "))
        Celsius = float(Kelvin - 273.15)
        print("{:.2f} Kelvin é igual a {:.2f} Celsius.".format(Kelvin, Celsius))
        os.system("pause")
    elif resp == 3:
        Rankine = float(input("Insira um valor: "))
        Celsius = float(((5*Rankine)/9)-273.15)
        print("{:.2f} Rankine é igual a {:.2f} Celsius.".format(Rankine, Celsius))
        os.system("pause")
    elif resp == 4:
        Réaumur = float(input("Insira um valor: "))
        Celsius = float((5*Réaumur)/4)
        print("{:.2f} Réaumur é igual a {:.2f} Celsius.".format(Réaumur, Celsius))
        os.system("pause")
    else:
        print('Opção invalida!')
        print('Tente de Novo!')
        os.system("pause")
    clearTerminal()
    printOptions()
    resp = int(input('Insira uma opção: '))
print("FIM!")