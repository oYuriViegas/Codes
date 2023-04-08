import random

def jokenpo(usuario, computador):
    if usuario == computador:
        return "Empate"
    elif (usuario == 0 and computador == 2) or (usuario == 1 and computador == 0) or (usuario == 2 and computador == 1):
        return "Usuário"
    else:
        return "Computador"

def jogar_jokenpo():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    pontos_usuario = 0
    pontos_computador = 0

    while True:
        computador = int(random.randint(0, 2))
        print("\nOpções: 0 - Pedra, 1 - Papel, 2 - Tesoura, 3 - Sair")
        escolha_usuario = input("Escolha uma opção: ")

        if escolha_usuario.isdigit() and 0 <= int(escolha_usuario) <= 3:
            escolha_usuario = int(escolha_usuario)
            if escolha_usuario == 3:
                break

            print(f"Usuário: {opcoes[escolha_usuario]}, Computador: {opcoes[computador]}")
            resultado = jokenpo(escolha_usuario, computador)

            if resultado == "Usuário":
                pontos_usuario += 1
                print("Usuário ganhou!")
            elif resultado == "Computador":
                pontos_computador += 1
                print("Computador ganhou!")
            else:
                print("Empate!")
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 0 e 3.")

        print(f"Pontuação: Usuário {pontos_usuario} x {pontos_computador} Computador")

if __name__ == "__main__":
    jogar_jokenpo()
