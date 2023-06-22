dados = [
    { "DOENCAS":"GRIPE","SINTOMAS":["TOSSE","CORIZA","FEBRE","DOR CORPO"]},
    { "DOENCAS":"DENGUE","SINTOMAS":["FEBRE","DOR CORPO"]},
    { "DOENCAS":"COVID","SINTOMAS":["FEBRE","TOSSE","FALTA AR"]},
    { "DOENCAS":"MALARIA","SINTOMAS":["FEBRE","CALAFRIO","MANCHA CORPO"]},
]

sintoma = input("Digite um sintoma: ").upper()

doencas = []
for doenca in dados:
    if sintoma in doenca["SINTOMAS"]:
        doencas.append(doenca["DOENCAS"])

if doencas:
    print("Doenças correspondentes ao sintoma informado:")
    for doenca in doencas:
        print(doenca)
else:
    print("Nenhuma doença encontrada com o sintoma informado.")
