import random


class Monstro:
    def __init__(self, nome, vida=50, ataque=8, defesa=3):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.iniciativa = 0

    def atacar(self, oponente):
        print(f"\n{self.nome} ataca {oponente.nome}!")
        dano = random.randint(1, self.ataque)
        print(f'\n{self.nome} atacou o {oponente.nome}, com {dano} de dano')
        oponente.receber_dano(dano)
        
    def receber_dano(self, dano):
        dano_recebido = max(0, dano)  # Garante que o dano recebido não será negativo
        self.vida = max(0, self.vida - dano_recebido)  # Garante que a vida não seja negativa
        print(f"\n{self.nome} recebeu {dano_recebido} de dano e agora tem "
              f"{self.vida} de vida")