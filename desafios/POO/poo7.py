"""
7.	Classe com lista interna
Enunciado:
 Classe Agenda que guarda uma lista de contatos.

"""
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Telefone: {self.telefone}")

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def exibir_contatos(self):
        for contato in self.contatos:
            contato.exibir_informacoes()

# Exemplo de uso
contato1 = Contato("Alice", "1234-5678")
contato2 = Contato("Bob", "9876-5432")

agenda = Agenda()
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.exibir_contatos()