def eh_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def verificar_data(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False

    if eh_bissexto(ano) and mes == 2:
        max_dias = 29
    elif mes == 2:
        max_dias = 28
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:
        max_dias = 31

    if dia < 1 or dia > max_dias:
        return False

    return True

# Pedindo ao usuário para inserir o dia, mês e ano
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verificando a consistência dos dados e se o ano é bissexto
if verificar_data(dia, mes, ano):
    if eh_bissexto(ano):
        print(f"A data {dia}/{mes}/{ano} é válida e o ano {ano} é bissexto.")
    else:
        print(f"A data {dia}/{mes}/{ano} é válida e o ano {ano} não é bissexto.")
else:
    print("A data inserida é inválida.")
