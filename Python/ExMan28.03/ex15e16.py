# Função para converter números de 1 a 9 em palavras
def converter_unidades(num):
    unidades = ["zero", "um", "dois", "três", "quatro",
                "cinco", "seis", "sete", "oito", "nove"]
    return unidades[num]

# Função para converter números de 10 a 19 em palavras
def converter_dezenas(num):
    dezenas = ["dez", "onze", "doze", "treze", "quatorze", "quinze",
            "dezesseis", "dezessete", "dezoito", "dezenove"]
    return dezenas[num - 10]

# Função para converter múltiplos de 10 (20, 30, 40, etc.) em palavras
def converter_dezenas_multiplos(num):
    dezenas_multiplos = ["", "", "vinte", "trinta", "quarenta", "cinquenta",
                        "sessenta", "setenta", "oitenta", "noventa"]
    return dezenas_multiplos[num]

# Função para converter múltiplos de 100 (100, 200, 300, etc.) em palavras
def converter_centenas_multiplos(num):
    centenas_multiplos = ["", "cento", "duzentos", "trezentos", "quatrocentos",
                        "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
    return centenas_multiplos[num]

# Função principal para converter um número inteiro entre 0 e 999 em palavras
def numero_por_extenso(num):
    if 1 <= num < 10:
        return converter_unidades(num)
    elif 10 <= num < 20:
        return converter_dezenas(num)
    elif 20 <= num < 100:
        if num % 10 == 0:
            return converter_dezenas_multiplos(num // 10)
        else:
            return converter_dezenas_multiplos(num // 10) + " e " + converter_unidades(num % 10)
    elif 100 <= num < 1000:
        if num % 100 == 0:
            if num == 100:
                return "cem"
            else:
                return converter_centenas_multiplos(num // 100)
        else:
            return converter_centenas_multiplos(num // 100) + " e " + numero_por_extenso(num % 100)
    else:
        return "zero"

# Função para converter um valor em dólares (com até duas casas decimais) em palavras
def dolares_por_extenso(valor):
    parte_inteira = int(valor)
    parte_decimal = round((valor - parte_inteira) * 100)

    extenso_inteiro = numero_por_extenso(parte_inteira) + " dólar(es)"
    extenso_decimal = numero_por_extenso(parte_decimal) + " centavo(s)"

    if parte_decimal == 0:
        return extenso_inteiro
    else:
        return extenso_inteiro + " e " + extenso_decimal

# Solicitando ao usuário para inserir um valor em dólares
while True:
    valor = float(input("Digite um valor em dólares entre 0 e 999 (até duas casas decimais): "))
    if 0 <= valor < 1000:
        break
    else:
        print("Por favor, insira um valor válido.")

# Imprimindo o valor em dólares por extenso
print(dolares_por_extenso(valor))
