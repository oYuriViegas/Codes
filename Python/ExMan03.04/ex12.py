def numeros_divisiveis_por_n(inicio, fim, n):
    divisiveis = []
    for i in range(inicio, fim + 1):
        if i % n == 0:
            divisiveis.append(i)
    return divisiveis

def main():
    inicio = int(input("Digite o valor inicial do intervalo: "))
    fim = int(input("Digite o valor final do intervalo: "))
    n = int(input("Digite o número para verificar a divisibilidade: "))
    
    divisiveis = numeros_divisiveis_por_n(inicio, fim, n)
    
    print(f"Números divisíveis por {n} no intervalo de {inicio} a {fim}:")
    for numero in divisiveis:
        print(numero)

if __name__ == "__main__":
    main()
