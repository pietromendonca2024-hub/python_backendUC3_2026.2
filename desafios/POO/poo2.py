"""
2.	Classe Aluno com método estudar
Enunciado:
 Crie uma classe Aluno que tenha nome e um método estudar() que imprime uma mensagem.
"""
class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def estudar(self):
        print(f"{self.nome} está estudando.")