menor_temperatura = 9999
dia_menor_temperatura = 0

for d in range(31):
    temperatura = (0.011 * (d**3)) - (0.3 * (d**2)) + (0.04 * d)

    if temperatura < menor_temperatura:
        menor_temperatura = temperatura
        dia_menor_temperatura = d

print(f"O dia com a menor temperatura prevista é {dia_menor_temperatura}, com temperatura de {menor_temperatura:.2f} graus Celsius.")
