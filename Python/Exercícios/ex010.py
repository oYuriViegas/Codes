n1 = int(input("Insira um número: "))
n2 = int(input("Insira um número: "))
n3 = int(input("Insira um número: "))

if n1 < n2 and n2 < n3:
    print("Os números estão em ordem crescente!")
elif n3 < n2 and n2 < n1:
    print("Os números estão em ordem decrescente!")
else:
    print("Os números não estão em ordem!")