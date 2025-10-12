from typing import List

class TelaSistema:
    def mostrar_menu_principal(self) -> str:
        print("\n=== SISTEMA DE VIAGENS ===")
        print("1 - Gerenciar Pessoas")
        print("2 - Gerenciar Empresas")
        print("3 - Gerenciar Viagens")
        print("4 - Gerenciar Pagamentos")
        print("5 - Ver Passeios Mais Populares")
        print("6 - Relatórios")
        print("9 - Popular com dados de teste")
        print("0 - Sair")
        return input("Escolha uma opção: ")

    def mostrar_passeios_populares(self, passeios: List[tuple]):
        print("\n--- Top 3 Passeios Mais Populares ---")
        if not passeios:
            print("Nenhum passeio cadastrado para gerar sugestões.")
            return
        
        for i, (atracao, contagem) in enumerate(passeios):
            print(f"{i+1}º: {atracao} (Registrado em {contagem} itinerário(s))")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")