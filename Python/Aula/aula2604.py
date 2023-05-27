import os

def menu():
    print("\nAGENDA TABAJARA")
    print("1 - CADASTRAR")
    print("2 - LISTAR")
    print("3 - CONSULTAR")
    print("4 - DELETAR")
    print("0 - SAIR")
    opcao = int(input("Qual a sua opção? "))
    return opcao

def cadastrar(contatos):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    telefone = input("Digite o telefone: ")
    contatos[nome] = {'idade': idade, 'telefone': telefone}

def listar(contatos):
    for nome, info in contatos.items():
        print(f"{nome} - Idade: {info['idade']} - Telefone: {info['telefone']}")

def consultar(contatos):
    nome = input("Digite o nome do contato: ")
    if nome in contatos:
        print(f"{nome} - Idade: {contatos[nome]['idade']} - Telefone: {contatos[nome]['telefone']}")
    else:
        print("Contato não encontrado.")

def deletar(contatos):
    nome = input("Digite o nome do contato que deseja deletar: ")
    if nome in contatos:
        del contatos[nome]
        print(f"Contato {nome} deletado com sucesso.")
    else:
        print("Contato não encontrado.")

def main():
    contatos_iniciais = {
        "Ana": {"idade": 25, "telefone": "1111-1111"},
        "Bruno": {"idade": 30, "telefone": "2222-2222"},
        "Carla": {"idade": 23, "telefone": "3333-3333"},
        "Diego": {"idade": 45, "telefone": "4444-4444"},
        "Eliana": {"idade": 34, "telefone": "5555-5555"},
        "Fernando": {"idade": 40, "telefone": "6666-6666"},
        "Gustavo": {"idade": 29, "telefone": "7777-7777"},
        "Helena": {"idade": 31, "telefone": "8888-8888"},
        "Igor": {"idade": 19, "telefone": "9999-9999"},
        "Julia": {"idade": 27, "telefone": "0000-0000"},
    }

    contatos = contatos_iniciais.copy()

    while True:
        opcao = menu()
        os.system('cls')
        if opcao == 0:
            break
        elif opcao == 1:
            cadastrar(contatos)
        elif opcao == 2:
            listar(contatos)
        elif opcao == 3:
            consultar(contatos)
        elif opcao == 4:
            deletar(contatos)
        else:
            print("Opção inválida. Tente novamente.")
        os.system('pause')

if __name__ == "__main__":
    main()
