from typing import List, Dict, Any
from Model.pessoa import Pessoa

class TelaPessoa:
    def mostrar_menu(self) -> str:
        print("\n--- Gerenciar Pessoas ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Voltar")
        return input("Escolha: ")

    def pegar_dados_cadastro(self) -> Dict[str, Any]:
        print("\n>> Cadastro de Pessoa")
        try:
            id = int(input("ID: "))
            nome = input("Nome: ")
            celular = input("Celular: ")
            identificacao = input("Identificação (CPF/RG): ")
            idade = int(input("Idade: "))
            return {"id": id, "nome": nome, "celular": celular, "identificacao": identificacao, "idade": idade}
        except ValueError:
            self.mostrar_mensagem("Erro: ID e Idade devem ser números.")
            return None

    def mostrar_lista(self, lista: List[Pessoa]):
        print("\n--- Lista de Pessoas ---")
        if not lista:
            print("Nenhuma pessoa cadastrada.")
            return
        for item in lista:
            print(f"ID: {item.id} | Nome: {item.nome} | Idade: {item.idade}")

    def pegar_id(self, acao: str) -> int:
        try:
            id = int(input(f"\nID da pessoa para {acao}: "))
            return id
        except ValueError:
            self.mostrar_mensagem("Erro: ID deve ser um número.")
            return None

    def pegar_dados_edicao(self) -> Dict[str, Any]:
        print("\n>> Edição de Pessoa (deixe em branco para manter)")
        nome = input("Novo nome: ")
        celular = input("Novo celular: ")
        idade_str = input("Nova idade: ")
        
        dados = {}
        if nome: dados['novo_nome'] = nome
        if celular: dados['novo_celular'] = celular
        if idade_str:
            try:
                dados['nova_idade'] = int(idade_str)
            except ValueError:
                self.mostrar_mensagem("Aviso: Idade inválida, não será alterada.")
        return dados

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")