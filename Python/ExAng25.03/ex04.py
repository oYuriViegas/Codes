S = 0

X = float(input("Insira o valor de X: "))

def factorial(n):
    result = 1
    for j in range(1, n, 1):
        result += result * j
    return result
1
for i in range(0, 3, 1):
    if i == 0:
        S = X
    else:
        numerator = X**(i*2)
        denominator = (i * 2) + 1
        if i % 2 == 0:
            S += numerator / factorial(denominator)
        else:
            S -= numerator / factorial(denominator)


print(f'O valor de S é : {S:.2f}')

