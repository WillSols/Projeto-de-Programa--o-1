from Controllers import ControladorPrincipal


class TelaPrincipal:
    def __init__(self):
        self.__controlador = ControladorPrincipal()

    def mostrar_menu(self):
        print("\n=== SISTEMA DE VIAGENS ===")
        print("1 - Gerenciar Pessoas")
        print("2 - Gerenciar Empresas")
        print("3 - Gerenciar Viagens")
        print("0 - Sair")

    def executar(self):
        while True:
            self.mostrar_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.menu_pessoas()
            elif opcao == "2":
                self.menu_empresas()
            elif opcao == "3":
                self.menu_viagens()
            elif opcao == "0":
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    #Pessoas
    def menu_pessoas(self):
        while True:
            print("\n--- MENU PESSOAS ---")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Editar")
            print("4 - Excluir")
            print("0 - Voltar")
            op = input("Escolha: ")

            if op == "1":
                self.cadastrar_pessoa()
            elif op == "2":
                self.listar_pessoas()
            elif op == "3":
                self.editar_pessoa()
            elif op == "4":
                self.excluir_pessoa()
            elif op == "0":
                break
            else:
                print("Opção inválida!")

    def cadastrar_pessoa(self):
        print("\nCadastro de Pessoa:")
        id = int(input("ID: "))
        nome = input("Nome: ")
        celular = input("Celular: ")
        identificacao = input("Identificação (CPF/RG): ")
        idade = int(input("Idade: "))
        self.__controlador.registrar_pessoa(id, nome, celular, identificacao, idade)
        print("✅ Pessoa cadastrada com sucesso!")

    def listar_pessoas(self):
        pessoas = self.__controlador.listar_pessoas()
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            return
        for p in pessoas:
            print(f"ID: {p.id} | Nome: {p.nome} | Idade: {p.idade} | Celular: {p.celular}")

    def editar_pessoa(self):
        id = int(input("ID da pessoa a editar: "))
        pessoa = self.__controlador.buscar_pessoa_por_id(id)
        if not pessoa:
            print("Pessoa não encontrada.")
            return
        novo_nome = input("Novo nome (ENTER p/ manter): ")
        novo_celular = input("Novo celular (ENTER p/ manter): ")
        nova_idade = input("Nova idade (ENTER p/ manter): ")
        self.__controlador.editar_pessoa(
            id,
            novo_nome if novo_nome else None,
            novo_celular if novo_celular else None,
            int(nova_idade) if nova_idade else None
        )
        print("✅ Pessoa atualizada!")

    def excluir_pessoa(self):
        id = int(input("ID da pessoa a excluir: "))
        if self.__controlador.excluir_pessoa(id):
            print("✅ Pessoa excluída.")
        else:
            print("Pessoa não encontrada.")

    # Empresas
    def menu_empresas(self):
        while True:
            print("\n--- MENU EMPRESAS ---")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Editar")
            print("4 - Excluir")
            print("0 - Voltar")
            op = input("Escolha: ")

            if op == "1":
                self.cadastrar_empresa()
            elif op == "2":
                self.listar_empresas()
            elif op == "3":
                self.editar_empresa()
            elif op == "4":
                self.excluir_empresa()
            elif op == "0":
                break
            else:
                print("Opção inválida!")

    def cadastrar_empresa(self):
        print("\nCadastro de Empresa:")
        id = int(input("ID: "))
        nome = input("Nome: ")
        cnpj = input("CNPJ: ")
        telefone = input("Telefone: ")
        self.__controlador.registrar_empresa(id, nome, cnpj, telefone)
        print("✅ Empresa cadastrada com sucesso!")

    def listar_empresas(self):
        empresas = self.__controlador.listar_empresas()
        if not empresas:
            print("Nenhuma empresa cadastrada.")
            return
        for e in empresas:
            print(f"ID: {e.id} | Nome: {e.nome} | CNPJ: {e.cnpj} | Telefone: {e.telefone}")

    def editar_empresa(self):
        id = int(input("ID da empresa a editar: "))
        empresa = self.__controlador.buscar_empresa_por_id(id)
        if not empresa:
            print("Empresa não encontrada.")
            return
        novo_nome = input("Novo nome (ENTER p/ manter): ")
        novo_cnpj = input("Novo CNPJ (ENTER p/ manter): ")
        novo_telefone = input("Novo telefone (ENTER p/ manter): ")
        self.__controlador.editar_empresa(
            id,
            novo_nome if novo_nome else None,
            novo_cnpj if novo_cnpj else None,
            novo_telefone if novo_telefone else None
        )
        print("✅ Empresa atualizada!")

    def excluir_empresa(self):
        id = int(input("ID da empresa a excluir: "))
        if self.__controlador.excluir_empresa(id):
            print("✅ Empresa excluída.")
        else:
            print("Empresa não encontrada.")

    # Viagens
    def menu_viagens(self):
        while True:
            print("\n--- MENU VIAGENS ---")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("4 - Excluir")
            print("0 - Voltar")
            op = input("Escolha: ")

            if op == "1":
                self.cadastrar_viagem()
            elif op == "2":
                self.listar_viagens()
            elif op == "4":
                self.excluir_viagem()
            elif op == "0":
                break
            else:
                print("Opção inválida!")

    def cadastrar_viagem(self):
        print("\nCadastro de Viagem:")
        id = int(input("ID: "))
        destino = input("Destino: ")
        data_inicio = input("Data de início (dd/mm/aaaa): ")
        data_fim = input("Data de término (dd/mm/aaaa): ")
        self.__controlador.registrar_viagem(id, destino, data_inicio, data_fim)
        print("✅ Viagem cadastrada com sucesso!")

    def listar_viagens(self):
        viagens = self.__controlador.listar_viagens()
        if not viagens:
            print("Nenhuma viagem cadastrada.")
            return
        for v in viagens:
            print(f"ID: {v.id} | Destino: {v.destino} | Início: {v.data_inicio} | Fim: {v.data_fim}")

    def excluir_viagem(self):
        id = int(input("ID da viagem a excluir: "))
        if self.__controlador.excluir_viagem(id):
            print("✅ Viagem excluída.")
        else:
            print("Viagem não encontrada.")


if __name__ == "__main__":
    tela = TelaPrincipal()
    tela.executar()
