imp = float(input("Insira o valor do IPTU: "))
anoIm = int(input("Insira o ano de construção do imovel: "))
anoAt = int(input("Insira o ano atual: "))

idadeIm = int(anoAt - anoIm)

if idadeIm < 5:
    print("Valor do IPTU: R${:.2f}".format(imp))
    print("Com 0% de desconto.")
elif idadeIm >= 5 and idadeIm < 20:
    imp = imp-(imp*0.15)
    print("Valor do IPTU: R${:.2f}".format(imp))
    print("Com 15% de desconto.")
elif idadeIm >= 20 and idadeIm < 40:
    imp = imp-(imp*0.25)
    print("Valor do IPTU: R${:.2f}".format(imp))
    print("Com 25% de desconto.")
elif idadeIm >= 40:
    imp = imp-(imp*0.30)
    print("Valor do IPTU: R${:.2f}".format(imp))
    print("Com 30% de desconto.")