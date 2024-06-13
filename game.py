import random
import pandas as pd
from jogador import Jogador
from armas import Espadas
from classes import Classe


class Game:
    def __init__(self):
        self.jogadores = []
        self.monstros = []
        
    
    def temAlguemVivo(jogadores):
        for jogador in jogadores:
            if jogador.vida_atual > 0:
                return True
        return False 

    
    def ler_arquivo_arma(self, caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            linhas = file.readlines()

        colunas = ['nome', 'valor', 'moeda', 'dano', 'tipo_de_dano', 'peso', 'medida_de_peso', 'propriedades']
        dados = []
        print()
        print(' '.join(colunas))
        for linha in linhas:
            linha = linha.strip()
            partes = linha.split(' ', 7)
            print(' '.join(partes))
            if len(partes) == 8:
                nome, valor, moeda, dano, tipo_de_dano, peso, medida_de_peso, propriedades = partes
                dados.append([nome, valor, moeda, dano, tipo_de_dano, peso, medida_de_peso, propriedades])

        df = pd.DataFrame(dados, columns=colunas)
        return df

    def escolher_espada(self, nome_espada, df):
        try:
            # Verifica se nome_espada está na primeira coluna
            linha = df[df.iloc[:, 0] == nome_espada]
            if not linha.empty:
                return linha.iloc[0]
            else:
                raise ValueError(f"O valor '{nome_espada}' não foi encontrado na primeira coluna.")
        except Exception as e:
            print(f"Erro: {e}")
            return None

    def escolher_tipo_espada(self):
        print("\nQual tipo de arma você quer usar?\n")
        print("1 - Armas Simples Corpo a Corpo")
        print("2 - Armas Simples a Distância")
        
        while True:
            tipo = input("\nQual sua escolha?: ")
            
            if tipo == '1':
                print("\nA tabela abaixo contém as armas que você pode escolher, digite o primeiro nome da arma para confirmar sua escolha")
                tipo_escolhido = self.ler_arquivo_arma('Armas_Simples_Corpo_a_Corpo.txt')
                while True:
                    try:
                        nome_espada = input('\nDigite o nome da arma da sua escolha: ').capitalize()
                        espada_escolhida = self.escolher_espada(nome_espada, tipo_escolhido)
                        
                        if espada_escolhida is None:
                            print("\nA arma escolhida não foi encontrada na lista. Verifique o nome e tente novamente.\n")
                            continue  # Tentar novamente se a escolha for inválida
                        
                        espada = Espadas(**espada_escolhida)
                        return espada
                    
                    except ValueError as ve:
                        print(f"\nErro: {ve}\n")
                    except KeyError:
                        print("\nA arma escolhida não foi encontrada na lista. Verifique o nome e tente novamente.\n")
            
            elif tipo == '2':
                print("\nA tabela abaixo contém as armas que você pode escolher, digite o primeiro nome da arma para confirmar sua escolha")
                tipo_escolhido = self.ler_arquivo_arma('Armas_Simples_a_Distancia.txt')
                while True:
                    try:
                        nome_espada = input('\nDigite o nome da arma da sua escolha: ').capitalize()
                        espada_escolhida = self.escolher_espada(nome_espada, tipo_escolhido)
                        
                        if espada_escolhida is None:
                            print("\nA arma escolhida não foi encontrada na lista. Verifique o nome e tente novamente.\n")
                            continue  # Tentar novamente se a escolha for inválida
                        
                        espada = Espadas(**espada_escolhida)
                        return espada
                    
                    except ValueError as ve:
                        print(f"\nErro: {ve}\n")
                    except KeyError:
                        print("\nA arma escolhida não foi encontrada na lista. Verifique o nome e tente novamente.\n")
            
            else:
                print("\nDigite uma opção válida!")
            
            
    def batalhar(self, jogadores, monstro):
        
        if not self.temAlguemVivo(jogadores):
            return False
        
        else:
            
            if monstro.nome == 'Goblin':
                print("\nMarchando a passos firmes, na vasta e indomável terra de Eldoria, "
                    "surge por entre a sombras um Goblin")
                print("\nUma batalha vai começar!")
                input("\nCaso esteja preparado Pressione ENTER")
                
            if monstro.nome == 'Esqueleto':
                print("\nProsseguindo a aventura,um novo oponente aparece em sobressalto"
                    "seu nome é Esqueleto")
                print("\nUma batalha vai começar!")
                input("\nCaso esteja preparado Pressione ENTER")
                
            if monstro.nome == 'Dragão':
                print("\nEis que é chegado o Desafio Final, prepare-se para a última"
                    "batalha épica que vai definir o destino de Eldoria")
                print("\nVocê vai enfrentar o DRAGÃO")
                print("\nUma batalha vai começar!")
                input("\nCaso esteja preparado Pressione ENTER")
            
            print(f"\nBatalha iniciada contra o {monstro.nome.upper()}!")
            round = 1
            
            ordem = {}
            for personagem in jogadores + [monstro]:
                ordem[personagem] = personagem.iniciativa + random.randint(1, 20)
            
            input("\nPressione ENTER para rolar os dados...")
            
            ordem_ordenada = sorted(ordem.items(), key=lambda x: x[1], reverse=True)
            
            print("\nOrdem de iniciativa:")
            for personagem, iniciativa in ordem_ordenada:
                print(f"{personagem.nome} - iniciativa: {iniciativa}")
            print()
            
            while monstro.vida > 0 and any(jogador.vida_atual > 0 for jogador in jogadores):
                print(f"\nRound {round}:")
                round += 1
                for jogador in jogadores:
                    print(f"\nO movimento pertence ao jogador {jogador.nome}")
                    print(f"\nO jogador {jogador.nome} tem {jogador.vida_atual} de vida")
                    if jogador.vida_atual > 0:
                        jogador.atacar(monstro)
                        if monstro.vida <= 0:
                            break
                    else:
                        print(f"\nO jogador {jogador.nome} já foi derrotado")
                if monstro.vida <= 0:
                    break
            
                monstro.atacar(random.choice(jogadores))
                print()
            
            if monstro.vida <= 0:
                print(f"{monstro.nome} derrotado!")
                return True
            else:
                print("\nTodos os jogadores foram derrotados. Fim de jogo!")
                return False
            
    def criar_jogadores(self):
        jogadores = int(input('Quantos jogadores irao jogar?: '))
        lista_jogadores = []
        for i in range(1,jogadores+1):
            nome = input(f'Qual será o nome do Jogador {i}?: ')
            #Indica quais classes existem para que o jogador escolja uma delas
            classe = input(f'Qual será a classe do Jogador {i}?: \n1- Guerreiro\n2- Mago\n')
            if classe == 1:
                classe = Classe('Guerreiro', 12, 7)
                print(f'O Jogador escolheu ser um Guerreiro!')
            else:
                classe = Classe('Mago', 6, 4)
                print(f'O Jogador escolheu ser um Mago!')
            espada =  self.escolher_tipo_espada()
            jogador = Jogador(nome, classe, espada)
            lista_jogadores.append(jogador)
        
        return lista_jogadores