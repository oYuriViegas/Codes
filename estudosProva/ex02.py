games= []

while n < 0:
    n = int(input("Insira a quantidade de games: "))

for i in range(n):
    nome=input("Insira o nome: ")
    empresa=input("Insira a empresa: ")
    ano=int(input("Insira o ano: "))
    preco=float(input("Insira o preço: "))
    games.append([nome, empresa, ano, preco])

emp= input("Empresa de busca: ")
anoi= int(input("Ano inicial: "))
anof= int(input("Ano final: "))

for aux in games:
    if games[1].upper() == emp.upper() and anoi <= games[2] <= anof:
        print()