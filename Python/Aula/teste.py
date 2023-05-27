def analisar_lista(listaNumeros):
    quantidade = len(listaNumeros)
    soma = sum(listaNumeros)
    media = soma / quantidade
    maior = max(listaNumeros)
    menor = min(listaNumeros)

    resultado = {
        'Quantidade' : quantidade,
        'Soma' : soma,
        'Media' : media,
        'Maior' : maior,
        'Menor' : menor
    }

    return resultado

entrada_lista_int = [int(num) for num in input("Insira uma lista de números inteiros separados por espaço: ").split()]

saida = analisar_lista(entrada_lista_int)

for chave, valor in saida.items():
    print(f"{chave}: {valor}")


