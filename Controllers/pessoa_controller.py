from typing import List
from Model.pessoa import Pessoa
from Views.tela_pessoa import TelaPessoa
from Exceptions.exceptions import EntidadeNaoEncontradaException, IDJaExistenteException

class ControladorPessoa:
    def __init__(self):
        self.__pessoas: List[Pessoa] = []
        self.__tela = TelaPessoa()

    def abrir_tela(self):
        while True:
            opcao = self.__tela.mostrar_menu().strip()
            try:
                if opcao == "1":
                    self.__cadastrar()
                elif opcao == "2":
                    self.__listar()
                elif opcao == "3":
                    self.__editar()
                elif opcao == "4":
                    self.__excluir()
                elif opcao == "0":
                    break
                else:
                    self.__tela.mostrar_mensagem("Opção inválida!")
            
            except (EntidadeNaoEncontradaException, IDJaExistenteException) as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Ocorreu um erro inesperado: {e}")

    def __cadastrar(self):
        dados = self.__tela.pegar_dados_cadastro()
        if dados:
            if any(p.id == dados["id"] for p in self.__pessoas):
                raise IDJaExistenteException("Pessoa", dados["id"])
            
            self.adicionar_pessoa(**dados)
            self.__tela.mostrar_mensagem("✅ Pessoa cadastrada com sucesso!")

    def __listar(self):
        self.__tela.mostrar_lista(self.__pessoas)
    
    def __editar(self):
        self.__listar()
        id_pessoa = self.__tela.pegar_id("editar")
        if id_pessoa is None: return

        pessoa_encontrada = self.buscar_por_id(id_pessoa)
        novos_dados = self.__tela.pegar_dados_edicao()
        self.editar_pessoa(pessoa_encontrada.id, **novos_dados)
        self.__tela.mostrar_mensagem("✅ Pessoa atualizada!")

    def __excluir(self):
        self.__listar()
        id_pessoa = self.__tela.pegar_id("excluir")
        if id_pessoa is None: return

        self.excluir_pessoa(id_pessoa)
        self.__tela.mostrar_mensagem("✅ Pessoa excluída.")

    def adicionar_pessoa(self, id: int, nome: str, celular: str, identificacao: str, idade: int) -> Pessoa:
        nova_pessoa = Pessoa(id, nome, celular, identificacao, idade)
        self.__pessoas.append(nova_pessoa)
        return nova_pessoa

    def listar_pessoas(self) -> List[Pessoa]:
        return self.__pessoas

    def buscar_por_id(self, id: int) -> Pessoa:
        for p in self.__pessoas:
            if p.id == id:
                return p
        raise EntidadeNaoEncontradaException("Pessoa", id)

    def editar_pessoa(self, id: int, novo_nome: str = None, novo_celular: str = None, nova_idade: int = None):
        pessoa = self.buscar_por_id(id)
        if novo_nome: pessoa.nome = novo_nome
        if novo_celular: pessoa.celular = novo_celular
        if nova_idade: pessoa.idade = nova_idade

    def excluir_pessoa(self, id: int):
        pessoa = self.buscar_por_id(id)
        self.__pessoas.remove(pessoa)