from typing import List, Optional
from Models import Pessoa, Viagem, Itinerario, Pagamento, Empresa, PasseioTuristico


class ControladorPrincipal:
    def __init__(self):
        self.pessoas: List[Pessoa] = []
        self.viagens: List[Viagem] = []
        self.empresas: List[Empresa] = []

    #Create
    def registrar_pessoa(self, id: int, nome: str, celular: str, identificacao: str, idade: int) -> Pessoa:
        pessoa = Pessoa(id, nome, celular, identificacao, idade)
        self.pessoas.append(pessoa)
        print(f"Pessoa registrada: {pessoa.nome}")
        return pessoa

    def registrar_empresa(self, id: int, nome: str, cnpj: str, telefone: str) -> Empresa:
        empresa = Empresa(id, nome, cnpj, telefone)
        self.empresas.append(empresa)
        print(f"Empresa registrada: {empresa.nome}")
        return empresa

    def registrar_viagem(self, id: int, destino: str, data_inicio: str, data_fim: str, pessoas: List[Pessoa]) -> Viagem:
        viagem = Viagem(id, destino, data_inicio, data_fim)
        for pessoa in pessoas:
            viagem.adicionar_pessoa(pessoa)
        self.viagens.append(viagem)
        print(f"Viagem registrada para {destino} com {len(pessoas)} pessoa(s).")
        return viagem

    #Read
    def listar_pessoas(self) -> List[Pessoa]:
        return self.pessoas

    def listar_empresas(self) -> List[Empresa]:
        return self.empresas

    def listar_viagens(self) -> List[Viagem]:
        return self.viagens

    def buscar_pessoa_por_id(self, id: int) -> Optional[Pessoa]:
        for pessoa in self.pessoas:
            if pessoa.id == id:
                return pessoa
        return None

    def buscar_empresa_por_id(self, id: int) -> Optional[Empresa]:
        for empresa in self.empresas:
            if empresa.id == id:
                return empresa
        return None

    def buscar_viagem_por_id(self, id: int) -> Optional[Viagem]:
        for viagem in self.viagens:
            if viagem.id == id:
                return viagem
        return None
    
    #Edit
    def editar_pessoa(self, id: int, novo_nome=None, novo_celular=None, nova_idade=None) -> bool:
        pessoa = self.buscar_pessoa_por_id(id)
        if pessoa:
            if novo_nome:
                pessoa.nome = novo_nome
            if novo_celular:
                pessoa.celular = novo_celular
            if nova_idade:
                pessoa.idade = nova_idade
            return True
        return False

    def editar_empresa(self, id: int, novo_nome=None, novo_cnpj=None, novo_telefone=None) -> bool:
        empresa = self.buscar_empresa_por_id(id)
        if empresa:
            if novo_nome:
                empresa.nome = novo_nome
            if novo_cnpj:
                empresa.cnpj = novo_cnpj
            if novo_telefone:
                empresa.telefone = novo_telefone
            return True
        return False


    # ---------------------- DELETE ----------------------
    def excluir_pessoa(self, id: int) -> bool:
        pessoa = self.buscar_pessoa_por_id(id)
        if pessoa:
            self.pessoas.remove(pessoa)
            return True
        return False

    def excluir_empresa(self, id: int) -> bool:
        empresa = self.buscar_empresa_por_id(id)
        if empresa:
            self.empresas.remove(empresa)
            return True
        return False

    def excluir_viagem(self, id: int) -> bool:
        viagem = self.buscar_viagem_por_id(id)
        if viagem:
            self.viagens.remove(viagem)
            return True
        return False