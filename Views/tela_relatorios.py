from typing import List, Dict
from Model.viagem import Viagem
from Model.passeio_turistico import PasseioTuristico

class TelaRelatorios:
    def mostrar_menu(self) -> str:
        print("\n--- Menu de Relatórios ---")
        print("1 - Viagens por Destino/Data")
        print("2 - Passeios Mais Caros/Baratos por Cidade")
        print("3 - Percentual de Uso dos Meios de Transporte")
        print("0 - Voltar ao Menu Principal")
        return input("Escolha uma opção: ")

    def pegar_filtros_viagem(self) -> Dict[str, str]:
        print("\n>> Filtros para Relatório de Viagens (deixe em branco para ignorar)")
        destino = input("Filtrar por destino: ")
        data_inicio = input("Filtrar por data de início (ex: 2025-12-10): ")
        return {"destino": destino, "data_inicio": data_inicio}

    def pegar_cidade_passeio(self) -> str:
        cidade = input("\nDigite a cidade para gerar o relatório de passeios: ")
        return cidade

    def mostrar_relatorio_viagens(self, viagens: List[Viagem]):
        print("\n--- Relatório: Viagens Filtradas ---")
        if not viagens:
            print("Nenhuma viagem encontrada com os filtros fornecidos.")
            return
        for v in viagens:
            nomes_participantes = [p.nome for p in v.pessoas]
            print(f"ID: {v.id} | Destinos: {v.destinos} | Datas: {v.data_inicio} a {v.data_fim}")
            print(f"   Participantes: {', '.join(nomes_participantes) or 'Nenhum'}")

    def mostrar_relatorio_passeios_preco(self, cidade: str, mais_caros: List[PasseioTuristico], mais_baratos: List[PasseioTuristico]):
        print(f"\n--- Relatório: Passeios em {cidade} ---")
        print("\n>> 3 Passeios MAIS CAROS:")
        if not mais_caros:
            print("Nenhum.")
        else:
            for p in mais_caros:
                print(f"- {p.atracao}: R${p.valor:.2f}")

        print("\n>> 3 Passeios MAIS BARATOS:")
        if not mais_baratos:
            print("Nenhum.")
        else:
            for p in mais_baratos:
                print(f"- {p.atracao}: R${p.valor:.2f}")

    def mostrar_relatorio_transportes(self, dados: Dict[str, float]):
        print("\n--- Relatório: Percentual de Uso dos Meios de Transporte ---")
        if not dados:
            print("Nenhum transporte registrado para gerar relatório.")
            return
        for tipo, percentual in dados.items():
            print(f"- {tipo}: {percentual:.2f}%")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")