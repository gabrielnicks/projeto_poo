from abc import ABC, abstractmethod
from typing import Optional
class Ser(ABC):

    @abstractmethod
    def atacar(self, oponente: Optional['Ser']) -> None:
        pass

    @abstractmethod
    def receber_dano(self, dano: int) -> None:
        pass
