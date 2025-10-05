from abc import ABC, abstractmethod
from typing import List


class Entidade(ABC):
    def __init__(self, id: int):
        self.id = id


class Pessoa(Entidade):
    def __init__(self, id: int, nome: str, celular: str, identificacao: str, idade: int):
        super().__init__(id)
        self.nome = nome
        self.celular = celular
        self.identificacao = identificacao
        self.idade = idade


class Viagem(Entidade):
    def __init__(self, id: int, destino: str, data_inicio: str, data_fim: str):
        super().__init__(id)
        self.destino = destino
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.pessoas: List[Pessoa] = []
        self.itinerarios: List["Itinerario"] = []
        self.pagamentos: List["Pagamento"] = []

    def adicionar_pessoa(self, pessoa: Pessoa):
        self.pessoas.append(pessoa)

    def adicionar_itinerario(self, itinerario: "Itinerario"):
        self.itinerarios.append(itinerario)

    def registrar_pagamento(self, pagamento: "Pagamento"):
        self.pagamentos.append(pagamento)


class Itinerario(Entidade):
    def __init__(self, id: int, cidade: str):
        super().__init__(id)
        self.cidade = cidade
        self.passeios: List["PasseioTuristico"] = []
        self.transportes: List["Transporte"] = []

    def adicionar_passeio(self, passeio: "PasseioTuristico"):
        self.passeios.append(passeio)

    def adicionar_transporte(self, transporte: "Transporte"):
        self.transportes.append(transporte)


class PasseioTuristico(Entidade):
    def __init__(self, id: int, cidade: str, atracao: str, horario_inicio: str,
                 horario_fim: str, valor: float, pessoa: Pessoa):
        super().__init__(id)
        self.cidade = cidade
        self.atracao = atracao
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        self.valor = valor
        self.pessoa = pessoa


class Transporte(Entidade, ABC):
    def __init__(self, id: int, tipo: str, empresa: "Empresa"):
        super().__init__(id)
        self.tipo = tipo
        self.empresa = empresa


class Empresa(Entidade):
    def __init__(self, id: int, nome: str, cnpj: str, telefone: str):
        super().__init__(id)
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone


class Pagamento(Entidade):
    def __init__(self, id: int, data: str, viagem: Viagem, pessoa: Pessoa,
                 valor_pago: float, modalidade: str):
        super().__init__(id)
        self.data = data
        self.viagem = viagem
        self.pessoa = pessoa
        self.valor_pago = valor_pago
        self.modalidade = modalidade  # dinheiro, pix, cartão
