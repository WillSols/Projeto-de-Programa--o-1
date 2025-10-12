# Views/tela_pagamento.py
from typing import List, Dict, Any
from Model.pagamento import Pagamento
from Model.viagem import Viagem
from Model.pessoa import Pessoa

class TelaPagamento:
    def mostrar_menu(self) -> str:
        print("\n--- Gerenciar Pagamentos ---")
        print("1 - Registrar Novo Pagamento")
        print("2 - Listar Pagamentos de uma Viagem")
        print("0 - Voltar")
        return input("Escolha: ")

    def pegar_dados_pagamento(self) -> Dict[str, Any]:
        print("\n>> Dados do Pagamento")
        try:
            id = int(input("ID do Pagamento: "))
            data = input("Data (ex: 2025-11-05): ")
            valor = float(input("Valor pago (ex: 500.00): "))
            modalidade = input("Modalidade (dinheiro, pix ou cartão): ")
            
            if modalidade not in ["dinheiro", "pix", "cartão"]:
                self.mostrar_mensagem("Modalidade inválida. Use 'dinheiro', 'pix' ou 'cartão'.")
                return None

            return {"id": id, "data": data, "valor_pago": valor, "modalidade": modalidade}
        except ValueError:
            self.mostrar_mensagem("Erro: ID e Valor devem ser números.")
            return None

    def mostrar_lista_viagens(self, viagens: List[Viagem]):
        print("\n--- Selecione a Viagem ---")
        if not viagens:
            print("Nenhuma viagem cadastrada.")
            return
        for v in viagens:
            print(f"ID: {v.id} | Destinos: {v.destinos}")

    def mostrar_lista_pessoas(self, pessoas: List[Pessoa]):
        print("\n--- Selecione a Pessoa ---")
        if not pessoas:
            print("Nenhuma pessoa nesta viagem.")
            return
        for p in pessoas:
            print(f"ID: {p.id} | Nome: {p.nome}")

    def mostrar_pagamentos(self, pagamentos: List[Pagamento]):
        print("\n--- Pagamentos Registrados ---")
        if not pagamentos:
            print("Nenhum pagamento registrado para esta viagem.")
            return
        total_pago = 0
        for pg in pagamentos:
            print(f"ID: {pg.id} | Data: {pg.data} | Pessoa: {pg.pessoa.nome} | Valor: R${pg.valor_pago:.2f} | Modalidade: {pg.modalidade}")
            total_pago += pg.valor_pago
        print(f"---------------------------------")
        print(f"Total Pago na Viagem: R${total_pago:.2f}")

    def pegar_id_generico(self, tipo_item: str) -> int:
        try:
            id = int(input(f"Digite o ID do(a) {tipo_item} desejado(a): "))
            return id
        except ValueError:
            self.mostrar_mensagem("Erro: ID deve ser um número.")
            return None

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")