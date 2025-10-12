from typing import List
from .entidade import Entidade
from .passeio_turistico import PasseioTuristico
from .transporte import Transporte

class Itinerario(Entidade):
    def __init__(self, id: int, cidade: str):
        super().__init__(id)
        self.cidade = cidade
        self.passeios: List[PasseioTuristico] = []
        self.transportes: List[Transporte] = []

    def adicionar_passeio(self, passeio: PasseioTuristico):
        self.passeios.append(passeio)

    def adicionar_transporte(self, transporte: Transporte):
        self.transportes.append(transporte)