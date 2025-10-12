from typing import List
from Model.viagem import Viagem
from Model.pessoa import Pessoa
from Model.itinerario import Itinerario
from Model.passeio_turistico import PasseioTuristico
from Model.transporte import Transporte
from Views.tela_viagem import TelaViagem
from .pessoa_controller import ControladorPessoa
from .empresa_controller import ControladorEmpresa
from Exceptions.exceptions import EntidadeNaoEncontradaException, IDJaExistenteException, RegraDeNegocioException

class ControladorViagem:
    def __init__(self, controlador_pessoa: ControladorPessoa, controlador_empresa: ControladorEmpresa):
        self.__viagens: List[Viagem] = []
        self.__tela = TelaViagem()
        self.__controlador_pessoa = controlador_pessoa
        self.__controlador_empresa = controlador_empresa

    def abrir_tela(self):
        while True:
            opcao = self.__tela.mostrar_menu().strip()
            try:
                if opcao == "1":
                    self.__cadastrar()
                elif opcao == "2":
                    self.__tela.mostrar_lista(self.__viagens)
                elif opcao == "3":
                    self.__detalhar_viagem()
                elif opcao == "0":
                    break
                else:
                    self.__tela.mostrar_mensagem("Opção inválida!")
            except (EntidadeNaoEncontradaException, IDJaExistenteException, RegraDeNegocioException) as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Ocorreu um erro inesperado: {e}")

    def __detalhar_viagem(self):
        self.__tela.mostrar_lista(self.__viagens)
        id_viagem = self.__tela.pegar_id_generico("viagem")
        if id_viagem is None: return
        
        viagem = self.buscar_viagem_por_id(id_viagem)

        while True:
            opcao = self.__tela.mostrar_menu_detalhes(viagem).strip()
            try:
                if opcao == "1":
                    self.__adicionar_itinerario(viagem)
                elif opcao == "2":
                    self.__tela.mostrar_itinerarios(viagem.itinerarios)
                elif opcao == "3":
                    self.__adicionar_passeio_ao_itinerario(viagem)
                elif opcao == "4":
                    self.__adicionar_transporte_ao_itinerario(viagem)
                elif opcao == "0":
                    break
                else:
                    self.__tela.mostrar_mensagem("Opção inválida!")
            except (EntidadeNaoEncontradaException, IDJaExistenteException) as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Ocorreu um erro inesperado: {e}")

    def __cadastrar(self):
        pessoas_disponiveis = self.__controlador_pessoa.listar_pessoas()
        dados = self.__tela.pegar_dados_cadastro(pessoas_disponiveis)
        if dados:
            if any(v.id == dados["id"] for v in self.__viagens):
                raise IDJaExistenteException("Viagem", dados["id"])

            ids_pessoas = dados.pop("ids_pessoas")
            pessoas_selecionadas = []
            
            for id_p in ids_pessoas:
                pessoa = self.__controlador_pessoa.buscar_por_id(id_p)
                if len(pessoa.viagens) >= 3:
                    raise RegraDeNegocioException(f"{pessoa.nome} já atingiu o limite de 3 viagens.")
                pessoas_selecionadas.append(pessoa)
            
            self.adicionar_viagem(**dados, pessoas=pessoas_selecionadas)
            self.__tela.mostrar_mensagem("✅ Viagem cadastrada com sucesso!")

    def __adicionar_itinerario(self, viagem: Viagem):
        dados = self.__tela.pegar_dados_itinerario()
        if dados:
            if any(it.id == dados["id"] for it in viagem.itinerarios):
                raise IDJaExistenteException("Itinerário", dados["id"])
            novo_itinerario = Itinerario(id=dados["id"], cidade=dados["cidade"])
            viagem.adicionar_itinerario(novo_itinerario)
            self.__tela.mostrar_mensagem("✅ Itinerário adicionado com sucesso!")

    def __adicionar_passeio_ao_itinerario(self, viagem: Viagem):
        self.__tela.mostrar_itinerarios(viagem.itinerarios)
        id_itinerario = self.__tela.pegar_id_generico("itinerário")
        if id_itinerario is None: return

        itinerario = next((it for it in viagem.itinerarios if it.id == id_itinerario), None)
        if not itinerario:
            raise EntidadeNaoEncontradaException("Itinerário", id_itinerario)

        dados = self.__tela.pegar_dados_passeio(viagem.pessoas)
        if dados:
            if any(p.id == dados["id"] for p in itinerario.passeios):
                raise IDJaExistenteException("Passeio", dados["id"])
            
            id_pessoa = dados.pop("id_pessoa")
            pessoa = self.__controlador_pessoa.buscar_por_id(id_pessoa)
            
            novo_passeio = PasseioTuristico(**dados, pessoa=pessoa)
            itinerario.adicionar_passeio(novo_passeio)
            self.__tela.mostrar_mensagem("✅ Passeio adicionado ao itinerário!")

    def __adicionar_transporte_ao_itinerario(self, viagem: Viagem):
        self.__tela.mostrar_itinerarios(viagem.itinerarios)
        id_itinerario = self.__tela.pegar_id_generico("itinerário")
        if id_itinerario is None: return

        itinerario = next((it for it in viagem.itinerarios if it.id == id_itinerario), None)
        if not itinerario:
            raise EntidadeNaoEncontradaException("Itinerário", id_itinerario)

        empresas = self.__controlador_empresa.listar_empresas()
        dados = self.__tela.pegar_dados_transporte(empresas)
        if dados:
            if any(t.id == dados["id"] for t in itinerario.transportes):
                raise IDJaExistenteException("Transporte", dados["id"])

            id_empresa = dados.pop("id_empresa")
            empresa = self.__controlador_empresa.buscar_empresa_por_id(id_empresa)
            
            novo_transporte = Transporte(**dados, empresa=empresa)
            itinerario.adicionar_transporte(novo_transporte)
            self.__tela.mostrar_mensagem("✅ Transporte adicionado ao itinerário!")

    def adicionar_viagem(self, id: int, destinos: str, data_inicio: str, data_fim: str, pessoas: List[Pessoa]) -> Viagem:
        nova_viagem = Viagem(id, destinos, data_inicio, data_fim)
        for p in pessoas:
            nova_viagem.adicionar_pessoa(p)
        self.__viagens.append(nova_viagem)
        return nova_viagem

    def listar_viagens(self) -> List[Viagem]:
        return self.__viagens

    def buscar_viagem_por_id(self, id: int) -> Viagem:
        for v in self.__viagens:
            if v.id == id:
                return v
        raise EntidadeNaoEncontradaException("Viagem", id)