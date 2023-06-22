#Exercício 01 : Ler o modelo de n veículos, armazená-los em memória e listá-los no console do terminal.

#
while True:
    try:
        numberVehicles = int(input("Insira quantos veículos serão registrados: "))
        if numberVehicles <= 0:
            print("Por favor, insira um número válido de veículos (maior que zero).")
        else:
            break
    except ValueError:
        print("Por favor, insira um número válido de veículos (apenas dígitos).")

vehiclesData = {}

for i in range(0, numberVehicles):
    key = (f'Veículo {i}')

    brand = input('Insira a marca do veículo: ')
    model = input('Insira o modelo do veículo: ')
    numberPlate = input('Insira o número da placa: ')
    vehiclesData[key] = [brand, model, numberPlate]

print('Veículos registrados\n')

for key, values in vehiclesData.items():
    brand, model, numberPlate = values
    print(f'{key+1}: \nMarca: {brand}, Modelo: {model}, Placa: {numberPlate}\n')