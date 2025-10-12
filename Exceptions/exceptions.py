class SistemaException(Exception):
    pass

class EntidadeNaoEncontradaException(SistemaException):
    def __init__(self, tipo_entidade: str, id: int):
        super().__init__(f"{tipo_entidade} com ID {id} não encontrado(a).")

class IDJaExistenteException(SistemaException):
    def __init__(self, tipo_entidade: str, id: int):
        super().__init__(f"Já existe um(a) {tipo_entidade} com o ID {id}.")

class RegraDeNegocioException(SistemaException):
    def __init__(self, mensagem: str):
        super().__init__(mensagem)