n_terms = 50
S = 0

for i in range(1, n_terms + 1):
    numerator = 2 * i - 1
    denominator = i
    S += numerator / denominator

print(f'O valor de S é: {S:.2f}')
