import random
from abc import ABC, abstractmethod


class Armas(ABC):
    @abstractmethod
    def ataque_rapido(self) -> int:
        pass

    @abstractmethod
    def ataque_lento(self) -> int:
        pass

    @abstractmethod
    def acertar(self) -> int:
        pass


class Espadas(Armas):
    def __init__(self, nome, valor, moeda, dano, tipo_de_dano, peso, medida_de_peso, propriedades):
        self.nome = nome
        self.valor = valor
        self.moeda = moeda
        self.dano = dano
        self.tipo_de_dano = tipo_de_dano
        self.peso = peso
        self.medida_de_peso = medida_de_peso
        self.propriedades = propriedades

    def acertar(self):
        return random.randint(1, self.acerto)

    def ataque_rapido(self):
        vezes = int(self.dano[0])
        dano = int(self.dano[2:])
        total = vezes * random.randint(1, dano)
        return total

    def ataque_lento(self):
        vezes = int(self.dano[0])
        dano = int(self.dano[2:])
        total = 2 * vezes * random.randint(1, dano // 2)
        return total


class ArcoFlecha(Armas):
    def __init__(self, nome, dano, acerto):
        self.nome = nome
        self.dano = dano
        self.acerto = acerto

    def acertar(self):
        return random.randint(1, self.acerto)

    def ataque_rapido(self):
        return random.randint(1, self.dano)

    def ataque_lento(self):
        return random.randint(1, self.dano // 2) + random.randint(1, self.dano // 2)


class Magias(Armas):
    def __init__(self, nome, dano, acerto):
        self.nome = nome
        self.dano = dano
        self.acerto = acerto

    def acertar(self):
        return random.randint(1, self.acerto)

    def ataque_rapido(self):
        return random.randint(1, self.dano)

    def ataque_lento(self):
        return random.randint(1, self.dano // 2) + random.randint(1, self.dano // 2)
