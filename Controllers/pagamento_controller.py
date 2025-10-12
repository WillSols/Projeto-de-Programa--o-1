from Model.pagamento import Pagamento
from Views.tela_pagamento import TelaPagamento
from .viagem_controller import ControladorViagem
from .pessoa_controller import ControladorPessoa
from Exceptions.exceptions import EntidadeNaoEncontradaException, IDJaExistenteException

class ControladorPagamento:
    def __init__(self, controlador_viagem: ControladorViagem, controlador_pessoa: ControladorPessoa):
        self.__tela = TelaPagamento()
        self.__controlador_viagem = controlador_viagem
        self.__controlador_pessoa = controlador_pessoa

    def abrir_tela(self):
        while True:
            opcao = self.__tela.mostrar_menu().strip()
            try:
                if opcao == "1":
                    self.__registrar()
                elif opcao == "2":
                    self.__listar()
                elif opcao == "0":
                    break
                else:
                    self.__tela.mostrar_mensagem("Opção inválida!")
            
            except (EntidadeNaoEncontradaException, IDJaExistenteException) as e:
                self.__tela.mostrar_mensagem(f"Erro: {e}")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Ocorreu um erro inesperado: {e}")

    def __registrar(self):
        viagens = self.__controlador_viagem.listar_viagens()
        self.__tela.mostrar_lista_viagens(viagens)
        if not viagens: return

        id_viagem = self.__tela.pegar_id_generico("viagem")
        if id_viagem is None: return
        viagem = self.__controlador_viagem.buscar_viagem_por_id(id_viagem)

        self.__tela.mostrar_lista_pessoas(viagem.pessoas)
        if not viagem.pessoas: return

        id_pessoa = self.__tela.pegar_id_generico("pessoa")
        if id_pessoa is None: return
        
        pessoa_encontrada = False
        for p in viagem.pessoas:
            if p.id == id_pessoa:
                pessoa = p
                pessoa_encontrada = True
                break
        
        if not pessoa_encontrada:
            raise EntidadeNaoEncontradaException("Pessoa (nesta viagem)", id_pessoa)

        dados_pagamento = self.__tela.pegar_dados_pagamento()
        if dados_pagamento:
            if any(p.id == dados_pagamento["id"] for p in viagem.pagamentos):
                raise IDJaExistenteException("Pagamento", dados_pagamento["id"])

            novo_pagamento = Pagamento(**dados_pagamento, viagem=viagem, pessoa=pessoa)
            viagem.registrar_pagamento(novo_pagamento)
            self.__tela.mostrar_mensagem("✅ Pagamento registrado com sucesso!")

    def __listar(self):
        viagens = self.__controlador_viagem.listar_viagens()
        self.__tela.mostrar_lista_viagens(viagens)
        if not viagens: return

        id_viagem = self.__tela.pegar_id_generico("viagem")
        if id_viagem is None: return
        
        viagem = self.__controlador_viagem.buscar_viagem_por_id(id_viagem)
        self.__tela.mostrar_pagamentos(viagem.pagamentos)