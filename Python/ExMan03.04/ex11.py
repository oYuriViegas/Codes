def numeros_divisiveis_por_3(inicio, fim):
    divisiveis = []
    for i in range(inicio, fim + 1):
        if i % 3 == 0:
            divisiveis.append(i)
    return divisiveis

def main():
    inicio = int(input("Digite o valor inicial do intervalo: "))
    fim = int(input("Digite o valor final do intervalo: "))
    
    divisiveis = numeros_divisiveis_por_3(inicio, fim)
    
    print(f"Números divisíveis por 3 no intervalo de {inicio} a {fim}:")
    for numero in divisiveis:
        print(numero)

if __name__ == "__main__":
    main()
