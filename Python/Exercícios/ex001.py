import os
def clearTerminal():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')
clearTerminal()
password = int(input('Escolha uma senha: '))
clearTerminal()
verify = int(input('Insira a senha: '))
while verify != password:
    print('Senha Incorreta! Tente Novamente!')
    os.system('pause')
    clearTerminal()
    verify = int(input('Insira a senha: '))
print('Senha Correta!\nAcesso liberado!')