def exibe(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(map(str, linha)))

def verifica_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(c == jogador for c in linha):
            if all(c == jogador for c in linha):
                return True
    
    for coluna in range(3):
        if all(tabuleiro[linha][coluna]== jogador for linha in range(3)):
            return True
    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False

def jogo_da_velha():
    tabuleiro = [[' ' for _ in range (3)] for _ in range(3)]
    jogadores = ['X', 'O']
    jogador_atual = 0

    while True:
        exibe(tabuleiro)
        linha = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a linha (0 a 2): "))
        coluna = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a coluna (0 a 2): "))

        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogadores[jogador_atual]
            if verifica_vitoria(tabuleiro, jogadores[jogador_atual]):
                exibe(tabuleiro)
                print(f"Jogador {jogadores[jogador_atual]} venceu!")
                break
            jogador_atual = 1 - jogador_atual
        else:
            print("Essa posição já está ocupada. Tente novamente.")

if __name__ == '__main__':
    jogo_da_velha()