from typing import List, Dict, Any
from Model.viagem import Viagem
from Model.pessoa import Pessoa
from Model.itinerario import Itinerario
from Model.empresa import Empresa

class TelaViagem:
    def mostrar_menu(self) -> str:
        print("\n--- Gerenciar Viagens ---")
        print("1 - Cadastrar Viagem")
        print("2 - Listar Viagens")
        print("3 - Detalhar Viagem / Gerenciar Itinerário")
        print("0 - Voltar")
        return input("Escolha: ")

    def mostrar_menu_detalhes(self, viagem: Viagem) -> str:
        print(f"\n--- Gerenciando a Viagem para: {viagem.destinos} (ID: {viagem.id}) ---")
        print("1 - Adicionar Itinerário")
        print("2 - Listar Itinerários (com detalhes)")
        print("3 - Adicionar Passeio a um Itinerário")
        print("4 - Adicionar Transporte a um Itinerário")
        print("0 - Voltar")
        return input("Escolha uma opção: ")

    def pegar_id_generico(self, tipo_item: str) -> int:
        try:
            id = int(input(f"\nDigite o ID do(a) {tipo_item} que deseja selecionar: "))
            return id
        except ValueError:
            self.mostrar_mensagem(f"Erro: ID de {tipo_item} deve ser um número.")
            return None

    def pegar_dados_itinerario(self) -> Dict[str, Any]:
        print("\n>> Novo Itinerário")
        try:
            id = int(input("ID do Itinerário: "))
            cidade = input("Cidade do Itinerário: ")
            return {"id": id, "cidade": cidade}
        except ValueError:
            self.mostrar_mensagem("Erro: ID deve ser um número.")
            return None

    def pegar_dados_passeio(self, pessoas_da_viagem: List[Pessoa]) -> Dict[str, Any]:
        print("\n>> Novo Passeio Turístico")
        try:
            id = int(input("ID do Passeio: "))
            cidade = input("Cidade: ")
            atracao = input("Atração: ")
            horario_inicio = input("Horário de início (ex: 09:00): ")
            horario_fim = input("Horário de fim (ex: 12:00): ")
            valor = float(input("Valor (ex: 150.75): "))
            
            print("\nSelecione a pessoa para este passeio:")
            for p in pessoas_da_viagem:
                print(f"  ID: {p.id} | Nome: {p.nome}")
            id_pessoa = int(input("ID da Pessoa: "))

            return {
                "id": id, "cidade": cidade, "atracao": atracao, "horario_inicio": horario_inicio,
                "horario_fim": horario_fim, "valor": valor, "id_pessoa": id_pessoa
            }
        except ValueError:
            self.mostrar_mensagem("Erro: ID, Valor e ID da Pessoa devem ser números.")
            return None

    def pegar_dados_transporte(self, empresas: List[Empresa]) -> Dict[str, Any]:
        print("\n>> Novo Transporte/Trecho")
        try:
            id = int(input("ID do Transporte: "))
            tipo = input("Tipo (ex: Avião, Trem, Carro): ")
            
            print("\nSelecione a empresa responsável:")
            for e in empresas:
                print(f"  ID: {e.id} | Nome: {e.nome}")
            id_empresa = int(input("ID da Empresa: "))

            return {"id": id, "tipo": tipo, "id_empresa": id_empresa}
        except ValueError:
            self.mostrar_mensagem("Erro: IDs devem ser números.")
            return None

    def mostrar_itinerarios(self, itinerarios: List[Itinerario]):
        print("\n--- Itinerários da Viagem ---")
        if not itinerarios:
            print("Nenhum itinerário cadastrado para esta viagem.")
            return
        for it in itinerarios:
            print(f"\nID: {it.id} | Cidade: {it.cidade}")
            if it.passeios:
                for p in it.passeios:
                    print(f"  - Passeio: {p.atracao} (Pessoa: {p.pessoa.nome})")
            if it.transportes:
                for t in it.transportes:
                    print(f"  - Transporte: {t.tipo} (Empresa: {t.empresa.nome})")
            if not it.passeios and not it.transportes:
                print("  (Vazio)")

    def mostrar_lista(self, lista: List[Viagem]):
        print("\n--- Lista de Viagens ---")
        if not lista:
            print("Nenhuma viagem cadastrada.")
            return
        for item in lista:
            nomes_participantes = [p.nome for p in item.pessoas]
            print(f"ID: {item.id} | Destinos: {item.destinos}")
            print(f"   Participantes: {', '.join(nomes_participantes) or 'Nenhum'}")

    def pegar_dados_cadastro(self, pessoas_disponiveis: List[Pessoa]) -> Dict[str, Any]:
        print("\n>> Cadastro de Viagem")
        try:
            id = int(input("ID da Viagem: "))
            destinos = input("Destinos: ")
            data_inicio = input("Data de início (ex: 2025-10-11): ")
            data_fim = input("Data de término (ex: 2025-10-20): ")

            if not pessoas_disponiveis:
                self.mostrar_mensagem("Aviso: Nenhuma pessoa cadastrada para adicionar à viagem.")
                return None

            print("\nSelecione as pessoas para a viagem (digite os IDs separados por vírgula):")
            for p in pessoas_disponiveis:
                print(f"  ID: {p.id} | Nome: {p.nome}")
            
            ids_str = input("IDs dos participantes: ")
            ids_selecionados = [int(id_str.strip()) for id_str in ids_str.split(',')]
            
            return {
                "id": id, "destinos": destinos, "data_inicio": data_inicio, 
                "data_fim": data_fim, "ids_pessoas": ids_selecionados
            }
        except ValueError:
            self.mostrar_mensagem("Erro: ID e IDs de pessoas devem ser números.")
            return None

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")