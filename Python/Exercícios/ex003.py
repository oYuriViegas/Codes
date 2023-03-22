import os
def limparTerminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
limparTerminal()
num = int(input("Insira um número: "))
while num != 0:
    limparTerminal()
    if num % 2 == 0:
        print('Esse número é Par!')
    else:
        print('Esse número é Impar!')
    os.system('pause')
    limparTerminal()
    print('Digite o número "0" se desejar sair.')
    num = int(input("Insira outro número: "))