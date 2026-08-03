"""
1.	Crie uma classe PessoaCrie uma classe Pessoa
Enunciado:
 Crie uma classe Pessoa com nome e idade. Depois crie um objeto e imprima seus dados.
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")