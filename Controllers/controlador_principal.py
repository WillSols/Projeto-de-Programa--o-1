from Views.tela_sistema import TelaSistema
from .pessoa_controller import ControladorPessoa
from .empresa_controller import ControladorEmpresa
from .viagem_controller import ControladorViagem
from .pagamento_controller import ControladorPagamento
from .relatorios_controller import ControladorRelatorios
from datetime import date, time

# Imports do teste #
from Model.itinerario import Itinerario
from Model.passeio_turistico import PasseioTuristico
from Model.transporte import Transporte
from Model.pagamento import Pagamento
from collections import Counter

class ControladorPrincipal:
    def __init__(self):
        self.controlador_pessoa = ControladorPessoa()
        self.controlador_empresa = ControladorEmpresa()
        self.controlador_viagem = ControladorViagem(self.controlador_pessoa, self.controlador_empresa)
        self.controlador_pagamento = ControladorPagamento(self.controlador_viagem, self.controlador_pessoa)
        self.controlador_relatorios = ControladorRelatorios(self)
        self.tela_sistema = TelaSistema()

    def iniciar_sistema(self):
        while True:
            opcao = self.tela_sistema.mostrar_menu_principal().strip()
            try:
                if opcao == "1":
                    self.controlador_pessoa.abrir_tela()
                elif opcao == "2":
                    self.controlador_empresa.abrir_tela()
                elif opcao == "3":
                    self.controlador_viagem.abrir_tela()
                elif opcao == "4":
                    self.controlador_pagamento.abrir_tela()
                elif opcao == "5":
                    self._sugerir_passeios_populares()
                elif opcao == "6":
                    self.controlador_relatorios.abrir_tela()
                elif opcao == "9":
                    self.inicializar_dados_teste()
                elif opcao == "0":
                    self.tela_sistema.mostrar_mensagem("Encerrando o sistema...")
                    break
                else:
                    self.tela_sistema.mostrar_mensagem("Opção inválida!")
            
            except Exception as e:
                self.tela_sistema.mostrar_mensagem(f"Ocorreu um erro fatal e inesperado: {e}")
    
    def _sugerir_passeios_populares(self):
        todas_as_viagens = self.controlador_viagem.listar_viagens()
        contagem_passeios = Counter()

        for viagem in todas_as_viagens:
            for itinerario in viagem.itinerarios:
                for passeio in itinerario.passeios:
                    contagem_passeios[passeio.atracao] += 1
        
        top_3_passeios = contagem_passeios.most_common(3)
        self.tela_sistema.mostrar_passeios_populares(top_3_passeios)

    def inicializar_dados_teste(self):
        self.tela_sistema.mostrar_mensagem("Populando sistema com um conjunto completo de dados de teste...")

        # Limpa dados antigos para evitar duplicatas
        self.controlador_pessoa._ControladorPessoa__pessoas.clear()
        self.controlador_empresa._ControladorEmpresa__empresas.clear()
        self.controlador_viagem._ControladorViagem__viagens.clear()
        
        # --- Pessoas ---
        p1 = self.controlador_pessoa.adicionar_pessoa(101, "João Silva", "48999998888", "123.456.789-00", 30)
        p2 = self.controlador_pessoa.adicionar_pessoa(102, "Maria Souza", "48988887777", "987.654.321-11", 28)
        p3 = self.controlador_pessoa.adicionar_pessoa(103, "Carlos Pereira", "48977776666", "111.222.333-44", 45)
        p4 = self.controlador_pessoa.adicionar_pessoa(104, "Ana Costa", "48966665555", "444.555.666-77", 25)

        # --- Empresas ---
        e_latam = self.controlador_empresa.adicionar_empresa(201, "LATAM Airlines", "11.222.333/0001-44", "0800-123-4567")
        e_trem = self.controlador_empresa.adicionar_empresa(202, "TremBala", "44.555.666/0001-77", "0800-987-6543")
        e_carro = self.controlador_empresa.adicionar_empresa(203, "Localiza Rent a Car", "77.888.999/0001-00", "0800-111-2222")
        
        # --- Viagem 1: Europa (Paris/Roma) ---
        v_europa = self.controlador_viagem.adicionar_viagem(301, "Paris e Roma", date(2025, 12, 10), date(2025, 12, 20), [p1, p2])
        
        it_paris = Itinerario(id=401, cidade="Paris")
        v_europa.adicionar_itinerario(it_paris)
        
        tr_aviao_ida = Transporte(id=501, tipo="Avião", empresa=e_latam)
        pa_eiffel = PasseioTuristico(id=601, cidade="Paris", atracao="Torre Eiffel", horario_inicio=time(9, 0), horario_fim=time(11, 0), valor=150.0, pessoa=p1)
        pa_louvre = PasseioTuristico(id=602, cidade="Paris", atracao="Museu do Louvre", horario_inicio=time(14, 0), horario_fim=time(18, 0), valor=200.0, pessoa=p2)
        pa_barco = PasseioTuristico(id=607, cidade="Paris", atracao="Passeio de Barco no Sena", horario_inicio=time(19, 0), horario_fim=time(20, 0), valor=85.50, pessoa=p1)
        it_paris.adicionar_transporte(tr_aviao_ida)
        it_paris.adicionar_passeio(pa_eiffel)
        it_paris.adicionar_passeio(pa_louvre)
        it_paris.adicionar_passeio(pa_barco)

        it_roma = Itinerario(id=402, cidade="Roma")
        v_europa.adicionar_itinerario(it_roma)

        tr_trem = Transporte(id=502, tipo="Trem", empresa=e_trem)
        pa_coliseu = PasseioTuristico(id=603, cidade="Roma", atracao="Coliseu", horario_inicio=time(10, 0), horario_fim=time(13, 0), valor=180.0, pessoa=p1)
        it_roma.adicionar_transporte(tr_trem)
        it_roma.adicionar_passeio(pa_coliseu)

        v_europa.registrar_pagamento(Pagamento(id=701, data=date(2025, 10, 1), valor_pago=1000.0, modalidade="pix", pessoa=p1, viagem=v_europa))
        v_europa.registrar_pagamento(Pagamento(id=702, data=date(2025, 10, 5), valor_pago=1500.0, modalidade="cartão", pessoa=p2, viagem=v_europa))
        v_europa.registrar_pagamento(Pagamento(id=703, data=date(2025, 10, 10), valor_pago=300.0, modalidade="dinheiro", pessoa=p1, viagem=v_europa))

        # --- Viagem 2: Japão (Tóquio) ---
        v_japao = self.controlador_viagem.adicionar_viagem(302, "Tóquio", date(2026, 3, 15), date(2026, 3, 25), [p3, p4])
        it_toquio = Itinerario(id=403, cidade="Tóquio")
        v_japao.adicionar_itinerario(it_toquio)

        tr_aviao2 = Transporte(id=503, tipo="Avião", empresa=e_latam)
        pa_torre_tokyo = PasseioTuristico(id=604, cidade="Tóquio", atracao="Tokyo Tower", horario_inicio=time(10, 0), horario_fim=time(12, 0), valor=120.0, pessoa=p3)
        pa_coliseu2 = PasseioTuristico(id=605, cidade="Tóquio", atracao="Coliseu", horario_inicio=time(15, 0), horario_fim=time(17, 0), valor=190.0, pessoa=p4)
        it_toquio.adicionar_transporte(tr_aviao2)
        it_toquio.adicionar_passeio(pa_torre_tokyo)
        it_toquio.adicionar_passeio(pa_coliseu2)
        
        # --- Viagem 3: Brasil ---
        v_brasil = self.controlador_viagem.adicionar_viagem(303, "Rio de Janeiro", date(2026, 7, 1), date(2026, 7, 8), [p1, p4])
        it_rio = Itinerario(id=404, cidade="Rio de Janeiro")
        v_brasil.adicionar_itinerario(it_rio)
        
        tr_carro = Transporte(id=504, tipo="Carro", empresa=e_carro)
        pa_cristo = PasseioTuristico(id=606, cidade="Rio de Janeiro", atracao="Cristo Redentor", horario_inicio=time(9, 0), horario_fim=time(11, 0), valor=90.0, pessoa=p4)
        it_rio.adicionar_transporte(tr_carro)
        it_rio.adicionar_passeio(pa_cristo)

        # --- Viagens 4 e 5 para teste da regra de negócio ---
        self.controlador_viagem.adicionar_viagem(304, "Nova York", date(2027, 1, 20), date(2027, 1, 27), [p4])

        self.tela_sistema.mostrar_mensagem("Dados de teste carregados com sucesso!")