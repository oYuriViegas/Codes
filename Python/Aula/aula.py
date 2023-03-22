import random
import os

# Gera um número inteiro aleatório entre 0 e 100
numero_secreto = random.randint(0, 100)
tentativas = 0

print("Bem-vindo ao jogo 'Adivinhe o número'!")
print("Estou pensando em um número entre 0 e 100. Tente adivinhar!")

# Loop principal do jogo
while True:
    os.system("cls")
    try:
        # Solicita que o usuário insira um palpite
        chute = int(input("Digite o seu palpite: "))
    except ValueError:
        # Se o usuário não inserir um número inteiro, exibe uma mensagem de erro e continua o loop
        print("Por favor, insira um número inteiro.")
        continue

    # Incrementa o contador de tentativas
    tentativas += 1

    # Verifica se o palpite do usuário é igual ao número secreto
    if chute == numero_secreto:
        # Se o usuário acertar, exibe uma mensagem de sucesso e encerra o loop
        print(f"Parabéns! Você acertou! O número era {numero_secreto}.")
        print(f"Você precisou de {tentativas} tentativas para acertar.")
        break
    # Verifica se o palpite do usuário é menor que o número secreto
    elif chute < numero_secreto:
        # Se o palpite for menor, exibe uma mensagem informando e continua o loop
        print("Seu palpite é menor do que o número secreto. Tente novamente!")
        os.system("pause")
    else:
        # Se o palpite for maior, exibe uma mensagem informando e continua o loop
        print("Seu palpite é maior do que o número secreto. Tente novamente!")
        os.system("pause")