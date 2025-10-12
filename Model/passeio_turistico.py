from .entidade import Entidade
from .pessoa import Pessoa

class PasseioTuristico(Entidade):
    def __init__(self, id: int, cidade: str, atracao: str, horario_inicio: str, horario_fim: str, valor: float, pessoa: Pessoa):
        super().__init__(id)
        self.cidade = cidade
        self.atracao = atracao
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        self.valor = valor
        self.pessoa = pessoa