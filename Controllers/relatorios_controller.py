from collections import Counter
from Views.tela_relatorios import TelaRelatorios
from Exceptions.exceptions import EntidadeNaoEncontradaException

class ControladorRelatorios:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela = TelaRelatorios()

    def abrir_tela(self):
        while True:
            opcao = self.__tela.mostrar_menu().strip()
            try:
                if opcao == "1":
                    self.__relatorio_viagens_por_filtro()
                elif opcao == "2":
                    self.__relatorio_passeios_por_preco()
                elif opcao == "3":
                    self.__relatorio_uso_meios_transporte()
                elif opcao == "0":
                    break
                else:
                    self.__tela.mostrar_mensagem("Opção inválida!")
            
            except EntidadeNaoEncontradaException as e:
                self.__tela.mostrar_mensagem(f"Erro ao gerar relatório: {e}")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Ocorreu um erro inesperado: {e}")

    def __relatorio_viagens_por_filtro(self):
        filtros = self.__tela.pegar_filtros_viagem()
        viagens = self.__controlador_principal.controlador_viagem.listar_viagens()
        
        viagens_filtradas = []
        for v in viagens:
            match_destino = (not filtros["destino"]) or (filtros["destino"].lower() in v.destinos.lower())
            match_data = (not filtros["data_inicio"]) or (filtros["data_inicio"] == v.data_inicio)
            
            if match_destino and match_data:
                viagens_filtradas.append(v)
        
        self.__tela.mostrar_relatorio_viagens(viagens_filtradas)

    def __relatorio_passeios_por_preco(self):
        cidade = self.__tela.pegar_cidade_passeio()
        if not cidade:
            self.__tela.mostrar_mensagem("Nome da cidade não pode ser vazio.")
            return

        viagens = self.__controlador_principal.controlador_viagem.listar_viagens()
        passeios_na_cidade = []

        for v in viagens:
            for it in v.itinerarios:
                for p in it.passeios:
                    if p.cidade.lower() == cidade.lower():
                        passeios_na_cidade.append(p)
        
        passeios_na_cidade.sort(key=lambda p: p.valor)
        
        mais_baratos = passeios_na_cidade[:3]
        mais_caros = passeios_na_cidade[-3:][::-1]

        self.__tela.mostrar_relatorio_passeios_preco(cidade, mais_caros, mais_baratos)

    def __relatorio_uso_meios_transporte(self):
        viagens = self.__controlador_principal.controlador_viagem.listar_viagens()
        todos_transportes = []
        
        for v in viagens:
            for it in v.itinerarios:
                todos_transportes.extend(it.transportes)

        total = len(todos_transportes)
        if total == 0:
            self.__tela.mostrar_relatorio_transportes({})
            return
        
        contagem = Counter(t.tipo for t in todos_transportes)
        percentuais = {tipo: (qtde / total) * 100 for tipo, qtde in contagem.items()}
        
        self.__tela.mostrar_relatorio_transportes(percentuais)