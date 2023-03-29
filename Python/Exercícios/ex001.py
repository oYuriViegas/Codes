import os

def clearTerminal():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

def showMenu():
    print("O que desja fazer?\n")
    print("1 - Alterar senha")
    print("2 - Acesso ao sistema")
    print("0 - Sair do menu\n")

clearTerminal()
password = "1234"
while True:
    clearTerminal()
    showMenu()
    verify = (input("Escolha uma opção: "))
    clearTerminal()
    if verify == "1":
        password = (input("Digite a nova senha: "))
        print("Senha Alterada!")
        os.system("pause")
    elif verify == "2":
        tryPass = (input("Insira a senha: "))
        if tryPass == password:
            print("Acesso permitido!")
            os.system("pause")
            break
        else:
            print("Acesso NEGADO!")
            os.system("pause")
            continue
    elif verify == "0":
        print("Saindo do Programa...")
        os.system("pause")
        break

