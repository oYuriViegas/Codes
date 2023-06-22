# Dataset contendo informações sobre jogos e características
jogos = [
    {"jogo": "The Witcher 3", "caracteristicas": {"RPG": 9, "Ação": 8, "Mundo Aberto": 10}},
    {"jogo": "FIFA 21", "caracteristicas": {"Esportes": 9, "Futebol": 10, "Modo Carreira": 8}},
    {"jogo": "Minecraft", "caracteristicas": {"Sandbox": 10, "Aventura": 7, "Criatividade": 9}},
    {"jogo": "Call of Duty: Warzone", "caracteristicas": {"FPS": 10, "Battle Royale": 9, "Multiplayer": 9}},
    {"jogo": "Animal Crossing: New Horizons", "caracteristicas": {"Simulação": 9, "Social": 8, "Customização": 10}},
    {"jogo": "Among Us", "caracteristicas": {"Multijogador": 9, "Intriga": 8, "Cooperação": 7}},
    {"jogo": "The Legend of Zelda: Breath of the Wild", "caracteristicas": {"Aventura": 10, "Exploração": 9, "Puzzle": 8}},
    {"jogo": "Fortnite", "caracteristicas": {"Battle Royale": 10, "Construção": 9, "Competitivo": 9}},
    {"jogo": "Assassin's Creed Valhalla", "caracteristicas": {"Ação": 9, "RPG": 8, "História": 9}},
    {"jogo": "Rocket League", "caracteristicas": {"Esportes": 8, "Carros": 9, "Competitivo": 10}}
]


def calcular_probabilidade(jogos, caracteristicas):
    """
    Calcula a probabilidade de cada jogo com base nas características fornecidas.
    
    Args:
        jogos (list): Lista de jogos com suas características e pesos.
        caracteristicas (list): Lista de características fornecidas pelo usuário.
    
    Returns:
        list: Lista de tuplas contendo o nome do jogo e sua probabilidade, ordenada em ordem decrescente de probabilidade.
    """
    probabilidades = []
    
    for jogo in jogos:
        total = sum(jogo["caracteristicas"].values())  # Calcula o total de pontos possíveis para todas as características do jogo
        
        peso_total = 0
        for c in caracteristicas:
            if c in jogo["caracteristicas"]:
                peso_total += jogo["caracteristicas"][c]  # Soma os pesos das características fornecidas pelo usuário presentes no jogo
        
        probabilidade = (peso_total / total) * 100  # Calcula a probabilidade de o jogo corresponder às características fornecidas
        
        probabilidades.append((jogo["jogo"], probabilidade))  # Adiciona o nome do jogo e sua probabilidade à lista de probabilidades
    
    return sorted(probabilidades, key=lambda x: x[1], reverse=True)  # Retorna a lista de probabilidades ordenada em ordem decrescente


def consultar_jogos():
    """
    Realiza a consulta das características do jogo fornecidas pelo usuário e exibe os resultados.
    """
    caracteristicas = []
    
    print("Informe três características do jogo:")
    for i in range(3):
        caracteristica = input(f"Característica {i+1}: ")
        caracteristicas.append(caracteristica)  # Armazena as características fornecidas pelo usuário
    
    resultados = calcular_probabilidade(jogos, caracteristicas)  # Chama a função calcular_probabilidade passando os jogos e as características
    
    print("\nResultados:")
    for jogo, probabilidade in resultados:
        print(f"{jogo}: {probabilidade:.1f}%")  # Imprime o nome do jogo e a sua probabilidade formatada em porcentagem


# Execução do programa
consultar_jogos()
