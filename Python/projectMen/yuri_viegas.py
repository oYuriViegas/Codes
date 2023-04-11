senha = "1234"
saldo_inicial = 0
while True:
    senha_correta = False
    total_vendas = 0
    total_itens = 0
    valor_total_vendas = 0

    while not senha_correta:
        senha_digitada = input("Digite a senha: ")
        if senha_digitada == senha:
            senha_correta = True
        else:
            print("Senha incorreta, tente novamente.")

    saldo_inicial = float(input("Digite o saldo inicial do caixa: "))
    saldo_atual = saldo_inicial

    while True:
        print("\nMenu:")
        print("1 - Registrar venda")
        print("2 - Encerrar e mostrar resumo")
        print("3 - Alterar senha")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_item = input("Digite o nome do item vendido: ")
            quantidade = int(input("Digite a quantidade vendida: "))
            valor_unitario = float(input("Digite o valor unitário do item: "))
            if valor_unitario < 0 or quantidade < 0:
                print("Valores inválidos.")
                continue
            valor_venda = valor_unitario * quantidade
            valor_recebido = float(input("Digite o valor recebido: "))
            troco = valor_recebido - valor_venda
            if troco < 0:
                print("Valor recebido insuficiente.")
                continue
            print("Troco: R$ {:.2f}".format(troco))
            saldo_atual += valor_venda
            total_vendas += 1
            total_itens += quantidade
            valor_total_vendas += valor_venda

        elif opcao == "2":
            break

        elif opcao == "3":
            while True:
                nova_senha = input("Digite a nova senha ou pressione ENTER para pular: ")
                if nova_senha != "":
                    senha = nova_senha
                    break
                else:
                    break

        else:
            print("Opção inválida, tente novamente.")

    print("\nResumo das vendas:")
    print("Total de vendas: ", total_vendas)
    print("Total de itens: ", total_itens)
    print("Valor total das vendas: R$ {:.2f}".format(valor_total_vendas))
    print("Saldo atual no caixa: R$ {:.2f}".format(saldo_atual))
