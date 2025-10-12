from typing import TYPE_CHECKING
from .entidade import Entidade
from .pessoa import Pessoa

if TYPE_CHECKING:
    from .viagem import Viagem

class Pagamento(Entidade):
    def __init__(self, id: int, data: str, valor_pago: float, modalidade: str, pessoa: Pessoa, viagem: "Viagem"):
        super().__init__(id)
        self.data = data
        self.valor_pago = valor_pago
        self.modalidade = modalidade
        self.pessoa = pessoa
        self.viagem = viagem