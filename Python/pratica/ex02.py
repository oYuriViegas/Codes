estoque = {
    'item1': 5,
    'item2': 0,
    'item3': 2
}

def verificar_estoque(item):
    if item in estoque:
        quantidade = estoque[item]
        if quantidade <= 0:
            print(f'O item: {item} está esgotado')
        else:
            print(f'A quantidade disponivel do item: {item} é {quantidade} unidades.')
    else:
        print(f'O item: {item} não está registrado')

consulta = input('Insira o nome do item a ser pesquisado: ')
verificar_estoque(consulta)