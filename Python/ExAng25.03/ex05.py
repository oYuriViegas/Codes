while True:
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    d = float(input("Digite o valor de d: "))
    e = float(input("Digite o valor de e: "))
    f = float(input("Digite o valor de f: "))

    # Verifica se todos os coeficientes a, b, c e d são iguais a zero
    if a == 0 and b == 0 and c == 0 and d == 0:
        print("Leitura de coeficientes interrompida.")
        break

    det = a * e - b * d
    if det == 0:
        print("Não é possível resolver o sistema. O determinante é igual a 0.")
    else:
        x = (c * e - b * f) / det
        y = (a * f - c * d) / det

        print(f'Solução: x = {x}, y = {y}')