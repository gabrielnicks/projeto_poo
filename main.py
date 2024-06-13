from game import Game
from monstro import Monstro

def game():
    # Inicializa o jogo
    jogo = Game()
    
    # Cria os jogadores
    jogadores = jogo.criar_jogadores()
    jogo.jogadores = jogadores
    
    # Lista de monstros
    monstros = [
        Monstro("Goblin", 50, 8, 3),
        Monstro("Esqueleto", 70, 10, 5),
        Monstro("Dragão", 150, 20, 10)
    ]
    
    # Conduz as batalhas
    for monstro in monstros:
        resultado = jogo.batalhar(jogo.jogadores, monstro)
        if not resultado:
            break

if __name__ == "__main__":
    game()