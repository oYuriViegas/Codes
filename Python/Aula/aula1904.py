import os
while True:
    cadastro = ['Andre', 'Luca', 'Predo', 'Ana', 'Nina', 'Beth', 'Gabriel', 'Felipe', 'Antenor', 'Juvenal', 'Yuri']

    print("Lista de cadastro:")
    for nome in cadastro:
        print(nome)

    nome = input("\nDigite um nome para verificar se está na lista: ")

    if nome in cadastro:
        print("O nome", nome, "está na lista.")
    else:
        print("O nome", nome, "não está na lista.")
        resp = input('Deseja cadastrar?<S/N>')
        if resp in ['S', 's']:
            cadastro.append(nome)
        elif resp in ['N', 'n']:
            print(f'Nome:{nome} nao será cadastrado')
    os.system('pause')
