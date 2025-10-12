from abc import ABC

class Entidade(ABC):
    def __init__(self, id: int):
        self.id = id