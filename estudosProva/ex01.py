dados = {
    2345 : {'nome' : 'caderno', 'preco' : float(20.00), 'estoque' : int(1000), 'desc': None, 'data': None},
    2564 : {'nome' : 'mochila', 'preco' : float(89.55), 'estoque' : int(200), 'desc': 10, 'data': [20, 6]},
    3213 : {'nome' : 'caneta bic', 'preco' : float(15.00), 'estoque' : int(2000), 'desc': 15, 'data': [5, 7]},
    3564 : {'nome' : 'borracha', 'preco' : float(2.55), 'estoque' : int(255), 'desc': None, 'data': None}
}

def lerProdutos(produtos: dict):
    n = int(input('Insira quantos produtos serão lidos: '))
    for i in range(n):
        print(f'Produto {i+1}\n')
        codigo = int(input('CODIGO: '))
        nome = input('NOME: ')
        preco = float(input('PREÇO: '))
        estoque = int(input('ESTOQUE: '))
        desc = input('DESCONTO: ')
        if desc == '':
            desc = None
        else:
            desc = int(desc)
        dia = input('DIA: ')
        mes = input('MES: ')
        if dia == '' or mes == '':
            data = None
        else:
            data = [int(dia), int(mes)]
        produtos[codigo] = {'nome': nome, 'preco': preco, 'estoque': estoque, 'desc': desc, 'data': data}
    return produtos

def imprimeClientesProdutosOferta(produtos: dict, dia: int, mes: int):
    for codigo, produto in produtos.items():
        if produto['data'] is not None:
            if produto['data'][1] < mes or (produto['data'][1] == mes and produto['data'][0] <= dia):
                print(f'{codigo} - {produto["nome"]} - {produto["preco"]} - {produto["estoque"]} - {produto["desc"]}')

def main():
    lerProdutos(dados)
    day = int(input('Insira o dia: '))
    month = int(input('Insira o mes: '))
    
    imprimeClientesProdutosOferta(dados, day, month)

main()

