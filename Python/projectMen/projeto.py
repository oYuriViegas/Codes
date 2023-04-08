import os

password = '12345'
verify = None

while verify != password:
    verify = input('Insira a senha para entrar no sistema: ')
    if verify == password:
        print('Acesso Liberado!')
        os.system('pause')
        os.system('cls')
        break
    print('Senha incorreta!\nAcesso Negado!')
    os.system('pause')
    os.system('cls')

print('Acesso')

""" os.system('pause')
os.system('cls')

resp = None

if verify == password:
    print('Acesso liberado!')
    resp = input('Deseja alterar a senha(y/n)?')
    if resp == 'y':
        password = input('Insira a nova senha: ')
        print('Senha alterada!')
        os.system('pause')
        os.system('cls')
        continue
    elif resp == 'n':
        print('Entrando no sistema...')
        os.system('pause')
        os.system('cls')
        break """