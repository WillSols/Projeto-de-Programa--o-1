from typing import List
from Model.empresa import Empresa
from Views.tela_empresa import TelaEmpresa
from Exceptions.exceptions import EntidadeNaoEncontradaException, IDJaExistenteException

class ControladorEmpresa:
    def __init__(self):
        self.__empresas: List[Empresa] = []
        self.__tela = TelaEmpresa()

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
            if any(e.id == dados["id"] for e in self.__empresas):
                raise IDJaExistenteException("Empresa", dados["id"])
            
            self.adicionar_empresa(**dados)
            self.__tela.mostrar_mensagem("✅ Empresa cadastrada com sucesso!")

    def __listar(self):
        self.__tela.mostrar_lista(self.__empresas)

    def __editar(self):
        self.__listar()
        id_empresa = self.__tela.pegar_id("editar")
        if id_empresa is None: return

        empresa_encontrada = self.buscar_empresa_por_id(id_empresa)
        novos_dados = self.__tela.pegar_dados_edicao()
        self.editar_empresa(empresa_encontrada.id, **novos_dados)
        self.__tela.mostrar_mensagem("✅ Empresa atualizada!")

    def __excluir(self):
        self.__listar()
        id_empresa = self.__tela.pegar_id("excluir")
        if id_empresa is None: return

        self.excluir_empresa(id_empresa)
        self.__tela.mostrar_mensagem("✅ Empresa excluída.")

    def adicionar_empresa(self, id: int, nome: str, cnpj: str, telefone: str) -> Empresa:
        nova_empresa = Empresa(id, nome, cnpj, telefone)
        self.__empresas.append(nova_empresa)
        return nova_empresa

    def listar_empresas(self) -> List[Empresa]:
        return self.__empresas

    def buscar_empresa_por_id(self, id: int) -> Empresa:
        for e in self.__empresas:
            if e.id == id:
                return e
        raise EntidadeNaoEncontradaException("Empresa", id)

    def editar_empresa(self, id: int, novo_nome: str = None, novo_cnpj: str = None, novo_telefone: str = None):
        empresa = self.buscar_empresa_por_id(id)
        if novo_nome: empresa.nome = novo_nome
        if novo_cnpj: empresa.cnpj = novo_cnpj
        if novo_telefone: empresa.telefone = novo_telefone

    def excluir_empresa(self, id: int):
        empresa = self.buscar_empresa_por_id(id)
        self.__empresas.remove(empresa)