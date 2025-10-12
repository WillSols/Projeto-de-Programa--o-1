from .entidade import Entidade

class Empresa(Entidade):
    def __init__(self, id: int, nome: str, cnpj: str, telefone: str):
        super().__init__(id)
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone