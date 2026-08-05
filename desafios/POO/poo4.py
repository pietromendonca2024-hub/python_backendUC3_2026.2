"""
4.	 Classe Produto e desconto
Enunciado:
 Crie classe Produto com preço e um método para aplicar desconto.
"""
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto

# Exemplo de uso
produto1 = Produto("Camiseta", 50.0)
print(f"Preço original: R$ {produto1.preco:.2f}")

produto1.aplicar_desconto(10)  # Aplica um desconto de 10%
print(f"Preço com desconto: R$ {produto1.preco:.2f}")