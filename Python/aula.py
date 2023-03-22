dia = int(input('Insira o dia: '))
mes = int(input('Insira o mes: '))
ano = int(input('Insira o ano: '))
if (dia<1) or (dia>31):
    print('ERRO: DIA DEVE SER UM NUMERO ENTRE 1 E 31')
elif (mes<1) or (mes>12):
    print('ERRO: MES DEVE SER UM NUMERO ENTRE 1 E 12')
elif (dia==31) and (mes in [4, 6, 9, 11]):
    print('ERRO: DIA 31 NAO PERTENCE AOS MESES DE ABRIL, JUNHO, SETEMBRO E NOVEMBRO')
elif (mes==2) and (dia>=30):
    print('ERRO: ME')
