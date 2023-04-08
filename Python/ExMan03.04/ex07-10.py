import random

def jogar_adivinhe_numero():
    numero_secreto = random.randint(0, 100)
    tentativas = 0
    desistiu = False

    print("Bem-vindo ao jogo 'Adivinhe o número'!")
    print("Estou pensando em um número entre 0 e 100.")
    
    while True:
        resposta = input("Digite o seu palpite ou 'desistir' para sair do jogo: ")

        if resposta.lower() == 'desistir':
            desistiu = True
            break

        palpite = int(resposta)
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns, você acertou o número {numero_secreto} em {tentativas} tentativas!")
            break
        elif palpite > numero_secreto:
            print("O número informado é maior do que o número secreto.")
        else:
            print("O número informado é menor do que o número secreto.")
            
    if desistiu:
        print(f"Você desistiu do jogo! O número secreto era {numero_secreto}.")
        return False
    else:
        return True

if __name__ == "__main__":
    jogando = True
    
    while jogando:
        jogando = jogar_adivinhe_numero()
        if jogando:
            resposta = input("Gostaria de jogar novamente? (s/n): ")
            if resposta.lower() != 's':
                jogando = False
