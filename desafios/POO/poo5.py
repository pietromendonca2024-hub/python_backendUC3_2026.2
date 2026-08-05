"""
5.	Classe Livro com status
Enunciado:
 Crie classe Livro com título e um atributo que diz se está disponível.

"""
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True  # Atributo que indica se o livro está disponível

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível.")