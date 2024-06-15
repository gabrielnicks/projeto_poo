import random
import InterfaceEspadas

class Espadas(InterfaceEspadas):
    def __init__(self, 
                 nome: str, 
                 valor: int, 
                 moeda: str, 
                 dano: str, 
                 tipo_de_dano: str, 
                 peso: float, 
                 medida_de_peso: str, 
                 propriedades: str) -> None:
        self.nome = nome
        self.valor = valor
        self.moeda = moeda
        self.dano = dano
        self.tipo_de_dano = tipo_de_dano
        self.peso = peso
        self.medida_de_peso = medida_de_peso
        self.propriedades = propriedades

    def ataque_rapido(self)-> int:
        vezes = int(self.dano[0])
        dano = int(self.dano[2:])
        total = vezes * random.randint(1, dano)
        return total

    def ataque_duas_maos(self)-> int:
        vezes = int(self.dano[0])
        dano = int(self.dano[2:])
        total = 2 * vezes * random.randint(1, dano // 2)
        return total
