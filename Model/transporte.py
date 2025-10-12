from .entidade import Entidade
from .empresa import Empresa

class Transporte(Entidade):
    def __init__(self, id: int, tipo: str, empresa: Empresa):
        super().__init__(id)
        self.tipo = tipo
        self.empresa = empresa