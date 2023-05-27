from bd import *
def menu():
    print('-----Aircheck-----\n')
    print('1 - Inserir amostras.')
    print('2 - Consultar amostras por ID.')
    print('3 - Remover amostras.')
    print('4 - Media das amostras.')
    print('5 - Exibir tabela completa.')
    print('0 - Sair.')
    print('\n')

    opcao = int(input('Opção: '))

    if opcao == 1:
        adicionar_amostra()
    elif opcao == 2:
        consultar_amostra()
    elif opcao == 4:
        imprimir_media_poluente()
    elif opcao == 5:
        imprimir_tabela_completa()
