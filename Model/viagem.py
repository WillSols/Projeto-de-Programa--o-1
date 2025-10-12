from typing import List
from .entidade import Entidade
from .pessoa import Pessoa
from .itinerario import Itinerario
from .pagamento import Pagamento
from datetime import date

class Viagem(Entidade):
    def __init__(self, id: int, destinos: str, data_inicio: date, data_fim: date):
        super().__init__(id)
        self.destinos = destinos
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.pessoas: List[Pessoa] = []
        self.itinerarios: List[Itinerario] = []
        self.pagamentos: List[Pagamento] = []

    def adicionar_pessoa(self, pessoa: Pessoa):
        if pessoa not in self.pessoas:
            self.pessoas.append(pessoa)
            pessoa.viagens.append(self)
            
    def adicionar_itinerario(self, itinerario: Itinerario):
        self.itinerarios.append(itinerario)

    def registrar_pagamento(self, pagamento: Pagamento):
        self.pagamentos.append(pagamento)