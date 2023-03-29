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

# Pedindo ao usuário para inserir um ano
ano = int(input("Digite um ano para verificar se é bissexto ou não: "))

# Verificando se o ano é bissexto e exibindo o resultado
if eh_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
