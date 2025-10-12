from typing import List, Dict, Any
from Model.empresa import Empresa

class TelaEmpresa:
    def mostrar_menu(self) -> str:
        print("\n--- Gerenciar Empresas ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Voltar")
        return input("Escolha: ")

    def pegar_dados_cadastro(self) -> Dict[str, Any]:
        print("\n>> Cadastro de Empresa")
        try:
            id = int(input("ID: "))
            nome = input("Nome: ")
            cnpj = input("CNPJ: ")
            telefone = input("Telefone: ")
            return {"id": id, "nome": nome, "cnpj": cnpj, "telefone": telefone}
        except ValueError:
            self.mostrar_mensagem("Erro: ID deve ser um número.")
            return None

    def mostrar_lista(self, lista: List[Empresa]):
        print("\n--- Lista de Empresas ---")
        if not lista:
            print("Nenhuma empresa cadastrada.")
            return
        for item in lista:
            print(f"ID: {item.id} | Nome: {item.nome} | CNPJ: {item.cnpj}")

    def pegar_id(self, acao: str) -> int:
        try:
            id = int(input(f"\nID da empresa para {acao}: "))
            return id
        except ValueError:
            self.mostrar_mensagem("Erro: ID deve ser um número.")
            return None

    def pegar_dados_edicao(self) -> Dict[str, Any]:
        print("\n>> Edição de Empresa (deixe em branco para manter)")
        nome = input("Novo nome: ")
        cnpj = input("Novo CNPJ: ")
        telefone = input("Novo telefone: ")
        
        dados = {}
        if nome: dados['novo_nome'] = nome
        if cnpj: dados['novo_cnpj'] = cnpj
        if telefone: dados['novo_telefone'] = telefone
        return dados

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")