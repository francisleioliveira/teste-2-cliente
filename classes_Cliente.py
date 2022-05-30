
from abc import ABC , abstractmethod
class Cliente(ABC):
    @abstractmethod
    def __init__(self,nome,endereco,telef):
        self.nome=nome
        self.endereco=endereco
        self.telef=telef
        pass





