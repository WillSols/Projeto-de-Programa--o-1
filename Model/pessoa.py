from typing import List, TYPE_CHECKING
from .entidade import Entidade

if TYPE_CHECKING:
    from .viagem import Viagem

class Pessoa(Entidade):
    def __init__(self, id: int, nome: str, celular: str, identificacao: str, idade: int):
        super().__init__(id)
        self.nome = nome
        self.celular = celular
        self.identificacao = identificacao
        self.idade = idade
        self.viagens: List["Viagem"] = []