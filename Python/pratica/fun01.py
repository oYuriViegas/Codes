"""Construir um programa que faz a leitura de N produtos (código: inteiro, descrição: string, quantidade: inteiro, preço:
real. Organizar os dados em um dicionário.
Após o trecho da leitura dos dados dos N produtos, fazer a leitura de um determinado código de produto e buscar o
produto com aquele código e, aumentar o preço do produto em 10%.
Imprimir os dados desse produto, antes e depois de ter seu preço aumentado."""

def inserir(n):
    dados = {}
    for i in range(n):
        print(f'Produto {i+1} \n')
        codigo = int(input("CÓDIGO: "))
        desc = input("DESCRIÇÃO: ")
        quant = int(input("QUANTIDADE: "))
        preco = float(input("PREÇO: "))
        print('\n')
        dados[codigo] = [desc, quant, preco]

    return dados

def procura(produto, codigo):
    if codigo in produto:
        return produto[codigo]
    else:
        return None
    
def aumentoPreco(list):
    preco = list[2]
    novo_preco = preco * 1.1
    return novo_preco

def main():
    qnt = int(input("Insira a quantidade de produtos: "))
    listaProduto = inserir(qnt)
    
    procura = int(input("Insira o código do produto a ser procurado: "))
    consulta = listaProduto[procura]

    print(f"\nDESCRIÇÃO: {consulta[0]}  -  QUANTIDADE: {consulta[1]}  -  PREÇO: {consulta[2]}")
    print(f"\n PREÇO COM AUMENTO DE 10%: {aumentoPreco(consulta)}")

main()