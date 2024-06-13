import random
from armas import Armas
from classes import Classe


class Jogador:
    def __init__(self, nome, classe: Classe, arma: Armas, defesa=5, nivel=1):
        self.classe = classe
        self.arma = arma
        self.atributos_random()
        self.nome = nome
        self.vida = self.modificador(self.constituicao) + self.classe.vida_base
        self.defesa = defesa
        self.nivel = nivel
        self.iniciativa = self.modificador(self.destreza)
        self.vida_atual = self.vida


    def upar(self):
        self.nivel += 1
        self.vida += self.classe.vida_level + self.modificador(self.constituicao)


    def modificador(self, x):
        return (x - 10) // 2


    def atributos_random(self):
        atributos = [random.randint(1, 20) for i in range(4)]
        atributos_mapping = ['forca', 'destreza', 'inteligencia', 'constituicao']
        
        print("\nVamos definir agora os atributos do seu personagem")
        input("\nPressione ENTER para a rolagem dos dados")
        print(f"\nVocê jogou os dados e obteve os seguintes valores: {atributos}")
        
        for i, atributo in enumerate(atributos_mapping):
            if atributo == 'constituicao':
                # Aloca automaticamente o último valor em constituição
                valor = atributos[0]
                setattr(self, atributo, valor)
                print(f"\nComo só sobrou o valor {valor}, ele foi alocado automaticamente em CONSTITUICAO")
                input("\nPressione ENTER para concluirmos")
            else:
                while True:
                    try:
                        valor = int(input(f"\nDefina qual desses valores você quer alocar em {atributo.upper()}: {atributos} "))
                        if valor in atributos:
                            setattr(self, atributo, valor)
                            atributos.remove(valor)
                            print(f"\nVocê alocou {valor} em {atributo.upper()}")
                            print(f"\nValores restantes: {atributos}")
                            break
                        else:
                            print("\nDigite um valor válido")
                    except ValueError:
                        print("\nPor favor, insira um número válido")


    def atacar(self, oponente):
        while True:
            try:
                ataque = int(input("\nFazer um ataque rápido ou 2 ataques lentos? Rapido - 1, Lento - 0: "))
                if ataque not in [0, 1]:
                    raise ValueError("Por favor, escolha apenas entre 0 ou 1.")
                break  # Se a entrada for válida, saia do loop
            except ValueError as ve:
                print(f"Erro: {ve}")
    
    
        dano = 0
        if ataque == 1:
            dano = self.arma.ataque_rapido() + self.modificador(self.forca)
        else:
            dano = self.arma.ataque_lento() + self.modificador(self.forca)
            
        print(f'{self.nome} atacou o {oponente.nome}, com {dano} de dano')
        oponente.receber_dano(dano)


    def receber_dano(self, dano):
        acerto = random.randint(1, 20)
        if acerto > self.defesa:
            dano_recebido = max(0, dano)  # Garante que o dano recebido não será negativo
            self.vida_atual = max(0, self.vida_atual - dano_recebido)  # Garante que a vida não seja negativa
            print(f"\n{self.nome} recebeu {dano_recebido} de dano e agora tem "
                  f"{self.vida_atual} de vida")
        else:
            print(f"\n{self.nome} desviou do ataque")
            
            
    def descansar(self):
        self.vida_atual = self.vida
        
    def apresentaJogador(self):
        print(f"\nO jogador {self.nome.upper()} pertence a classe {self.classe.nome.upper()}, empunha "
              f"a arma {self.arma.nome.upper()} e está pronto para a aventura!")