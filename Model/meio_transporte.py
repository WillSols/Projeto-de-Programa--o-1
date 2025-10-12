from .entidade import Entidade
from .passeio_turistico import EmpresaTransporte

class MeioTransporte(Entidade):
    def __init__(self, id: int, tipo: str, capacidade: int, empresa: EmpresaTransporte):
        super().__init__(id)
        self.tipo = tipo
        self.capacidade = capacidade
        self.empresa = empresa