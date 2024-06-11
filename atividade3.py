import json

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}'

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f'Contato {contato.nome} adicionado com sucesso!')

    def listar_contatos(self):
        if not self.contatos:
            print('Nenhum contato na agenda.')
        else:
            for contato in self.contatos:
                print(contato)

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                print(contato)
                return
        print('Contato não encontrado.')

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f'Contato {nome} removido com sucesso!')
                return
        print('Contato não encontrado.')

    def salvar_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as file:
            json.dump([contato.__dict__ for contato in self.contatos], file)
        print("Agenda salva com sucesso!")

    def carregar_de_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as file:
                contatos = json.load(file)
                self.contatos = [Contato(**contato) for contato in contatos]
            print("Agenda carregada com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado. Nenhum contato carregado.")

def menu():
    print("\nAgenda Telefônica")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato")
    print("4. Remover contato")
    print("5. Salvar agenda")
    print("6. Carregar agenda")
    print("7. Sair")
    return input("Escolha uma opção: ")

def obter_dados_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    return Contato(nome, telefone, email)

def main():
    agenda = Agenda()
    while True:
        opcao = menu()
        if opcao == '1':
            contato = obter_dados_contato()
            agenda.adicionar_contato(contato)
        elif opcao == '2':
            agenda.listar_contatos()
        elif opcao == '3':
            nome = input("Digite o nome do contato que deseja buscar: ")
            agenda.buscar_contato(nome)
        elif opcao == '4':
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)
        elif opcao == '5':
            nome_arquivo = input("Digite o nome do arquivo para salvar: ")
            agenda.salvar_em_arquivo(nome_arquivo)
        elif opcao == '6':
            nome_arquivo = input("Digite o nome do arquivo para carregar: ")
            agenda.carregar_de_arquivo(nome_arquivo)
        elif opcao == '7':
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
